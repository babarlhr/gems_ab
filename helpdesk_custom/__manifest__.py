{
    'name' : 'HelpDesk Custom',
    'description' : 'Helpdesk customization',
    'author' : 'Odoo Advantage Ireland',
    'website' : 'erp.odoo.ie',
    'data' : [
            'views/helpdesk_view.xml',
            'views/templates.xml',
            'views/helpdesk_forum_view.xml',
        ],
    'depends' : ['helpdesk','helpdesk_timesheet','mail','website_helpdesk_form'],
    'installable' : True,
}