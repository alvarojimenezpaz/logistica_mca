# -*- coding: utf-8 -*-
{
    'name': "Logística MCA Transportes",

    'summary': """
        Módulo que registra las guías de traslado de vehículos y sus
        correspondientes gastos""",

    'description': """
        Este módulo registra las guías de traslado de vehículos 
        identificando al cliente final, el vehículo, conductor,
        quien solicita, origen y destino, tipo de traslado, etc.
        A cada traslado se le asigna una rendición de gastos,
        en la que registran un depósito inicial y cada uno de los gastos.
    """,

    'author': "Álvaro Jiménez Paz",
    'website': "https://www.asinfo.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/logistica_mca_data.xml',
        'views/menu_views.xml',
        'views/tipos_rendicion_views.xml',
        'views/origen_views.xml',
        'views/destino_views.xml',
        'views/conductor_views.xml',
        'views/solicita_views.xml',
        'views/tipos_traslado_views.xml',
        'views/marcas_views.xml',
        'views/modelos_views.xml',
        'views/vehiculo_views.xml',
        'views/rendicion_views.xml',
        'views/rendicion_line_views.xml',
        'views/traslado_views.xml',
        'views/traslado_views.xml',
        'views/valortraslado_views.xml',
        'views/tipos_reclamo_views.xml',
        'views/tipos_siniestro_views.xml',
        'views/reclamo_views.xml',
        'views/reclamo_line_views.xml',
        'reports/traslado_template.xml',
        'reports/traslado_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
}
