# -*- coding: utf-8 -*-
{
    'name': 'Farmer Management',
    'version': '1.0',
    'summary': 'Brief description of the module',
    'description': '''
        Detailed description of the module
    ''',
    'category': 'Uncategorized',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/farmer_management_views.xml',
		'views/farmer_views.xml',
		'security/security.xml',
		'views/land_views.xml',
		'views/crop_views.xml',
		'views/family_views.xml',
],
'test': [
    'tests/test_farmer.py',
],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}