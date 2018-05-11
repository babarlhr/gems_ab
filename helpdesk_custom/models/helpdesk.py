from odoo import models, fields, api
from odoo import http

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    
#     user_id = fields.Many2one('res.users', string='Assigned to', track_visibility='onchange', default=lambda self:63, domain=lambda self: [('groups_id', 'in', self.env.ref('helpdesk.group_helpdesk_user').id)])
    description = fields.Html()
    
    @api.model
    def create(self, vals):
        ticket = super(HelpdeskTicket, self).create(vals)
        
        if not vals.get('user_id'):
            group_users = self.env['res.groups'].search([('category_id','=','Helpdesk'),('name','=','Manager')]).users
#             [user [for user.login in group_users]]
            
            template = self.env.ref('helpdesk_custom.example_email_template')
            for user_id in group_users:
#                 self.env['mail.template'].browse(template.id).send_mail(user_id.id, ticket.id, force_send=True)
                body_html = template.body_html.format(
                                                username=user_id.name,
                                                ticket_name=ticket.name,
                                                id=ticket.id,
                                                creator_name=ticket.create_uid.name,
                                                base_url=http.request.env['ir.config_parameter'].get_param('web.base.url'))
                subject = template.subject.format(name=ticket.name, ticket_no=" (#" + str(ticket.id) + ")")
                email_to = user_id.login
                mail_id = self.env['mail.mail'].create({
                                        'body_html' : body_html,
                                        'email_to' : email_to,
                                        'subject' : subject,
                                    })
                if mail_id:
                    mail_id.send()
                    self.env['mail.mail'].browse(mail_id.id).unlink()
        return ticket