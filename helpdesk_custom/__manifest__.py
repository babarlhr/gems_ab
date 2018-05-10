{
    'name' : 'HelpDesk Custom',
    'description' : 'Helpdesk customization',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'erp.odoo.ie',
    'data' : [
            'views/helpdesk_view.xml',
        ],
    'depends' : ['helpdesk','helpdesk_timesheet','mail'],
    'installable' : True,
}