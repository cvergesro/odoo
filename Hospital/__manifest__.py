# -*- coding: utf-8 -*-
{
    'name': "Hospital",  # Titulo del módulo
    'summary': "Gestionar pacients ",  # Resumen de la funcionaliadad
    'description': """
Gestor de pacients, metges i diagnosis
==============
    """,  

    #Indicamos que es una aplicación
    'author': "CELIA",
    'website': "http://iesjoanramis.org",
    'category': 'Project',
    'version': '1.0',
    'depends': ['base'],
    'application': True,

    'data': [
    # 'demo': [
        'security/ir.model.access.csv',
        'views/hospital_pacient.xml',
        'views/hospital_metge.xml',
        'views/hospital_diagnostic.xml',
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
