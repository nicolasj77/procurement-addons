# -*- encoding: utf-8 -*-
{
    'name': 'Computed Purchase Order',
    'version': '9.0.1',
    'category': 'Purchase Order',
    'description': """ todo """,
    'author': 'Coop IT Easy',
    'website': 'https://github.com/coopiteasy/procurement-addons',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'purchase',
        'stock',
        'stock_coverage',
    ],
    'data': [
        'views/computed_purchase_order.xml',
        'views/computed_purchase_order_wizard.xml',
    ],
}
