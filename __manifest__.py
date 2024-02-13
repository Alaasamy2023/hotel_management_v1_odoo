# -*- coding: utf-8 -*-
{
    'name': "hotel_management_v1",
    "version": "1.0.1",
    'sequence': -10000,

    "author": "https://alaa.my/",
    "license": "AGPL-3",
    "website": "https://alaa.my/",

    #'category': 'Accounting & Finance',
    'category': 'Sales',

    # any module necessary for this one to work correctly
    # 'depends': ['base','sale_management'],
    'depends': ['sale_management', 'account', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/room_reservation.xml',

        'views/HotelMeals.xml',

        'views/Rooms.xml',
        'views/HotelAmenity.xml',

        'views/AmenityTypes.xml',

        'views/HotelService.xml',

        'views/Service_Category.xml',

        'views/floor.xml',
        'views/menus.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
