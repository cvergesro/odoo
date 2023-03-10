# -*- coding: utf-8 -*-
{
    'name': "Cicles Formatius",  # Titulo del módulo
    'summary': "Cicles Formatius",  # Resumen de la funcionaliadad
    'description': """
Cicles Formatius
==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Celia Vergés Rodríguez",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
       
        'security/groups.xml',
        'security/ir.model.access.csv',
        
        #Cargamos los ficheros con vistas tanto de biblioteca_comic como de biblioteca_comic_categoria
        'views/cicle_formatiu.xml',
        'views/cicle_formatiu_modul.xml',
        'views/cicle_formatiu_profesor.xml',
        'views/cicle_formatiu_alumne.xml',
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
