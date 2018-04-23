# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class mail_activity(models.Model):
    _inherit = 'mail.activity'

    docs_approval = fields.Char(string="Docs Approval")