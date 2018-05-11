from odoo import models, fields, api
from odoo import http

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    
#     description = fields.Html()
    attachment_id = fields.One2many('ir.attachment','helpdesk_ticket_ids', string="Attachments")
    
    @api.model
    def default_get(self,default_fields):
        res = super(HelpdeskTicket, self).default_get(default_fields)
#         for group_d in self.env['res.users'].browse(self.env.user.id).groups_id:
#             if group_d.name == "Manager" and group_d.category_id.name == 'Helpdesk':
#                 res['is_helpdesk_manager'] = True
        
        user_id = self.env['res.users'].search([('name','=','Odoo@gems-ksa.com')])
        if user_id:
            res['user_id'] = user_id.id
            
        return res

#     @api.model
#     def create(self, vals):
#         ticket = super(HelpdeskTicket, self).create(vals)
#         
#         if not vals.get('user_id'):
#             team_member_ids = ticket.team_id.member_ids
#             template = self.env.ref('helpdesk_custom.example_email_template')
#             for user_id in team_member_ids:
#                 body_html = template.body_html.format(
#                                                 username=user_id.name,
#                                                 ticket_name=ticket.name,
#                                                 id=ticket.id,
#                                                 creator_name=ticket.create_uid.name,
#                                                 base_url=http.request.env['ir.config_parameter'].get_param('web.base.url'))
#                 subject = template.subject.format(name=ticket.name, ticket_no=" (#" + str(ticket.id) + ")")
#                 email_to = user_id.login
#                 mail_id = self.env['mail.mail'].create({
#                                         'body_html' : body_html,
#                                         'email_to' : email_to,
#                                         'subject' : subject,
#                                     })
#                 if mail_id:
#                     mail_id.send()
#                     self.env['mail.mail'].browse(mail_id.id).unlink()
#         return ticket