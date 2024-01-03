{
    'name': 'Movies',
    'version':'1.0.0',
    'sequence': -100,
    'depends': ['mail', 'product'],
    'category': 'Movies',
    'description': """Movies app""",
    'data':[
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/movies_view.xml',
        'views/res_partner_view.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}