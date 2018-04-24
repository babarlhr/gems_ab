from odoo import models, fields, api, _
import datetime

class DocumentControl(models.Model):
    _name="document.control"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _description = 'Document Control'
    _rec_name="name"
    
    name = fields.Char(string="Doc control Number", readonly=True,required=True, copy=False, index=True, default=lambda self: _('New'))
    requested_by = fields.Many2one('hr.employee', string="Requested By", readonly=True, default=lambda self: self.env.user.id)
    date_time = fields.Datetime('Date Time', readonly=True, default=fields.datetime.now())
    doc_type = fields.Selection([
                                ('msds', 'MSDS'),
                                ('method_statement', 'Method Statement'),
                                ('pme_sub', 'PME Submission'),
                                ('rc_sub', 'RC Submission'),
                                ('qa_doc', 'Q&A Documents'),
                                ('process_statment', 'Process Statment'),
                                ('reports', 'Reports'),
                                ('studies', 'Studies'),
                                ('correspondence', 'Correspondence'),
                                ('calc_sheet', 'Calculation sheet'),
                                ('model', 'Model'),
                                ('drawings', 'Drawings'),
                                ('presentation', 'Presentations'),
                                ('responsibility_matrix', 'Responsibility Matrix'),
                                ('review_verification_matrix', 'Review & verification Matrix')
                                ], string="Doc type")
#     doc_attachment = fields.Char('Doc Attachment')
    req_for = fields.Selection([
                            ('client', 'Client'),
                            ('regulator', 'Regulator'),
                            ('internal', 'Internal'),
                            ('other', 'Other'),
                                ], string="Req for")
    req_reference = fields.Char('Reference')
    doc_req_date = fields.Date('Doc Req date')
    initiation_doc_date = fields.Date('Initiation Doc date')
    
    description = fields.Text('Description')
    
    assign_to_manager = fields.Many2one('hr.employee', string="Assign to (Manager)", copy=False)
    assign_to_officer = fields.Many2one('hr.employee', string="Assign to (Officer)", copy=False)
    assign_datetime_manager = fields.Datetime(string="Assignment DateTime", copy=False,store=True)
    assign_datetime_officer = fields.Datetime(string="Assignment DateTime", copy=False)
    elapsed_days_m = fields.Char('Elapsed Days', compute="_compute_elapsed_days_m")
    elapsed_days_o = fields.Char('Elapsed Days', compute="_compute_elapsed_days_o")
    
    feedback_comment = fields.Text('Feedback')
    doc_ids = fields.One2many('ir.attachment', 'document_id', 'Documents')
#     doc_author = fields.Many2one('hr.employee', string="Author")
    
    approver_1 = fields.Many2one('res.users', inverse="_inverse_approval_by_group", string="Author", required=True)
    approver_2 = fields.Many2one('res.users', inverse="_inverse_approval_by_group", string="Reviewer", required=True)
    approver_3 = fields.Many2one('res.users', inverse="_inverse_approval_by_group", string="Approver", required=True)
    
    state = fields.Selection([
                            ('draft', 'New'),
                            ('approval_1', 'Author'),
                            ('approval_2', 'Reviewer'),
                            ('approval_3', 'Approver'),
                            ('done', 'Done'),
                            ('rejected', 'Rejected'),
                            ], readonly=True, string="States", track_visibility=True, default="draft", inverse="_inverse_send_notification_approve")
    
    # -- Approval States
    approval_state_1 = fields.Selection([
                                        ('pending','Pending'),
                                        ('hold','On-Hold'),
                                        ('done','Approved'),
                                        ('cancelled','Rejected')
                                    ], string="Author", default='pending', readonly=True)
    approval_state_2 = fields.Selection([
                                        ('pending','Pending'),
                                        ('hold','On-Hold'),
                                        ('done','Approved'),
                                        ('cancelled','Rejected')
                                    ], string="Reviewer", default='pending', readonly=True)
    approval_state_3 = fields.Selection([
                                        ('pending','Pending'),
                                        ('hold','On-Hold'),
                                        ('done','Approved'),
                                        ('cancelled','Rejected')
                                    ], string="Approver", default='pending', readonly=True)
    
    is_creator = fields.Boolean(compute='_compute_user_role', default=False)
    is_author = fields.Boolean(compute='_compute_user_role', default=False)
    is_reviewer = fields.Boolean(compute='_compute_user_role', default=False)
    is_approver = fields.Boolean(compute='_compute_user_role', default=False)
    
    @api.onchange('assign_to_manager')    
    def _compute_elapsed_days_m(self):
        if self.assign_datetime_manager:
            elapsed_days = fields.datetime.now() - datetime.datetime.strptime(self.assign_datetime_manager,'%Y-%m-%d %H:%M:%S')
            self.elapsed_days_m = elapsed_days.days
         
    @api.onchange('assign_to_officer')    
    def _compute_elapsed_days_o(self):
        if self.assign_datetime_officer:
            elapsed_days = (fields.datetime.now() - datetime.datetime.strptime(self.assign_datetime_officer,'%Y-%m-%d %H:%M:%S')).days
            self.elapsed_days_o = elapsed_days
    
    @api.multi
    @api.onchange('approver_1','approver_2','approver_3')
    def _compute_user_role(self):
        cid = self.env.uid
        for obj in self:
            if obj.approver_1.id == cid:
                obj.is_author = True
            if obj.approver_2.id == cid:
                obj.is_reviewer = True
            if obj.approver_3.id == cid:
                obj.is_approver = True
            if obj.create_uid.id == cid:
                obj.is_creator = True
    
    @api.multi
    def write(self, vals):
        if vals.get('assign_to_manager',False):
            vals['assign_datetime_manager'] = datetime.datetime.now()
        if vals.get('assign_to_officer',False):
            vals['assign_datetime_officer'] = datetime.datetime.now()
        if 'state' in vals:
            for rec in self:
                approval_type = False
                if rec.state == 'approval_1':
                    approval_type = 'Author'
                elif rec.state == 'approval_2':
                    approval_type = 'Reviewer'
                elif rec.state == 'approval_3':
                    approval_type = 'Approver'
                model_id = self.env.ref('document_control.model_document_control').id
                user_feedback=rec.feedback_comment
                try:
                    activity_type_id = self.env.ref('mail.mail_activity_data_todo').id
                except ValueError:
                    activity_type_id = False
                if approval_type:
                    activity_ids = self.env['mail.activity'].search([
                        ('docs_approval', '=', approval_type),
                        ('res_id', '=', rec.id),
                        ('res_model_id', '=', model_id),
                        ('activity_type_id', '=', activity_type_id)
                    ])
                    for activity_id in activity_ids:
                        activity_id.action_feedback(feedback=user_feedback)
                    rec.feedback_comment = ''
        return super(DocumentControl, self).write(vals)
            
    @api.model
    def create(self, vals):
        if vals.get('assign_to_manager',False):
            vals['assign_datetime_manager'] = datetime.datetime.now()
        if vals.get('assign_to_officer',False):
            vals['assign_datetime_officer'] = datetime.datetime.now()
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('document.control') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('document.control') or _('New')
        return super(DocumentControl, self).create(vals)
    
    @api.multi
    def states_approval(self):
        if self.state == "draft":
            self.write({
                'state' : 'approval_1',
            })
        elif self.state == "approval_1":
            self.write({
                'state' : 'approval_2',
                'approval_state_1' : 'done'
            })
        elif self.state == "approval_2":
            self.write({
                'state' : 'approval_3',
                'approval_state_2' : 'done'
            })
        elif self.state == "approval_3":
            self.write({
                'state' : 'done',
                'approval_state_3' : 'done'
            })
    
    @api.multi
    def set_to_rejected(self):
        if self.state == "approval_1":
            self.write({
                'state' : 'rejected',
                'approval_state_1' : 'cancelled'
            })
        elif self.state == "approval_2":
            self.write({
                'state' : 'rejected',
                'approval_state_2' : 'cancelled'
            })
        elif self.state == "approval_3":
            self.write({
                'state' : 'rejected',
                'approval_state_3' : 'cancelled'
            })
    
    @api.multi
    def set_states_back(self):
        if self.state == "approval_1":
            self.write({
                'state' : 'draft',
                'approval_state_1' : 'hold'
            })
        elif self.state == "approval_2":
            self.write({
                'state' : 'approval_1',
                'approval_state_2' : 'hold',
                'approval_state_1' : 'pending'
            })
        elif self.state == "approval_3":
            self.write({
                'state' : 'approval_2',
                'approval_state_3' : 'hold',
                'approval_state_2' : 'pending',
            })
        
#     Create an activity for the responsible person on state change.
    def _inverse_send_notification_approve(self):
        approval_type = None
        responsible_id = None
        approval_name = None
        if self.state == 'approval_1':
            if self.approver_1:
                responsible_id = self.approver_1
                approval_type = 'Author'
                approval_name = self.approver_1.partner_id
        elif self.state == 'approval_2':
            responsible_id = self.approver_2
            approval_type = 'Reviewer'
            approval_name = self.approver_2.partner_id
        elif self.state == 'approval_3':
            responsible_id = self.approver_3
            approval_type = 'Approver'
            approval_name = self.approver_3.partner_id
            
        if responsible_id:
            model_id = self.env.ref('document_control.model_document_control').id
            if approval_type:
                approval_user_name = _('<a href="#" data-oe-id="%s" data-oe-model="res.partner">%s</a>') % (approval_name.id, approval_name.name)
                message = _('Document Control "%s" is waiting for %s approval from %s .') % (self.name, approval_type, approval_user_name)
                self.message_post(
                    body=message,
                    partner_ids=[(4, responsible_id.partner_id.id)],
                    subtype='mail.mt_comment',
                    message_type="notification"
                )
                try:
                    activity_type_id = self.env.ref('mail.mail_activity_data_todo').id
                except ValueError:
                    activity_type_id = False
                activity = self.env['mail.activity'].create({
                    'activity_type_id': activity_type_id,
#                     'note': message,
                    'user_id': responsible_id.id,
                    'res_id': self.id,
                    'res_model_id': model_id,
                    'date_deadline': datetime.datetime.now().date(),
                    'docs_approval': approval_type
                })
                
#   Add users to the followers of the activity
    def _inverse_approval_by_group(self):
        for doc_control in self:
            partner_ids = []
            # -- Approver_1 MANAGER
            if doc_control.approver_1:
                partner_ids.append(doc_control.approver_1.partner_id.id)
            # -- Approver_2 MANAGER
            if doc_control.approver_2:
                partner_ids.append(doc_control.approver_2.partner_id.id)
            # -- Approver_3 Person
            if doc_control.approver_3:
                partner_ids.append(doc_control.approver_2.partner_id.id)

            partner_ids = list(set(partner_ids))
            doc_control.message_subscribe(partner_ids=partner_ids)
            
class IrAttachment(models.Model):
    _inherit = "ir.attachment"
    
    document_id = fields.Many2one('document.control', string="Documents")
    doc_author = fields.Many2one('hr.employee', string="Author")