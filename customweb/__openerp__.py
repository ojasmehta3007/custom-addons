{
    'name': 'Custom Web',
    'version': '1.0',
    'description':
        """

        """,
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
    'data': [
        'views/webclient_templates.xml',
    ],
    'bootstrap': True, # load translations for login screen
}
