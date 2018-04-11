from odoo import models, fields, api
from lxml import etree
from odoo.tools.safe_eval import safe_eval
from odoo.osv.orm import setup_modifiers

class HrEmployee(models.Model):
    _inherit = "hr.employee"
    
    state = fields.Selection([
                            ('unverified', 'Unverified'),
                            ('verified', 'Verified'),
                            ], readonly=True, copy=False, index=True, track_visibility='onchange', string="State", default='unverified')
    
    def verification(self):
        for rec in self:
            rec.state = 'verified'
            
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(HrEmployee, self).fields_view_get(view_id, view_type, toolbar=toolbar, submenu=submenu)
        if view_type=="form":
            doc = etree.XML(result['arch'])
            for node in doc.iter(tag="field"):
                if 'readonly' in node.attrib.get("modifiers",''):
                    attrs = node.attrib.get("attrs",'')
                    if 'readonly' in attrs:
                        attrs_dict = safe_eval(node.get('attrs'))
                        r_list = attrs_dict.get('readonly',)
                        if type(r_list)==list:
                            r_list.insert(0,('state','=','verified'))
                            if len(r_list) == 2:
                                r_list.insert(0,'|')
                            if len(r_list) > 2:
                                r_list.insert(2,'|')
                        attrs_dict.update({'readonly':r_list})
                        node.set('attrs', str(attrs_dict))
                        setup_modifiers(node, result['fields'][node.get("name")])
                        continue
                    else:
                        continue
                node.set('attrs', "{'readonly':[('state','=','verified')]}")
                setup_modifiers(node, result['fields'][node.get("name")])
                
            result['arch'] = etree.tostring(doc)
        return result