{

    'name': 'Tour Management',
    'version': '1.0',
    'category': 'Tours',
    "sequence": 1,
    'complexity': "easy",
    'description': """
        This module provide overall travel management system over OpenERP
        Features includes managing
        * Travel form
		* Vehicle Detail
		* Passenger Detail
		* City Detail
	    * Tour Details
    """,
    'author': 'Bista Solutions',
    'website': 'www.milantourandtravels.com',
    'depends': ['base','sale','product','website','website_sale'],
    'data': [
        'views/tour_query_view.xml',
        'views/tour_detail_view.xml',
        'views/meal_config.xml',
        'views/city_detail_view.xml',
        'views/package_itenary_view.xml',
        'views/hotel_detail_view.xml',
        'views/customer_detail_view.xml',
        'views/passenger_detail_view.xml',
        'views/vendor_detail_view.xml',
        'data/data.xml',
        'views/tour_detail_template_new.xml',
        'views/hotel_facility_view.xml',
        # 'views/query_code_view.xml',
        'views/google_spread_scheduler.xml'
        # 'views/res_company_view.xml',
        # 'views/query_code.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
