{
    'name': 'Dard Backend Theme',
    'version': '19.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Dark navy + orange backend theme with configurable branding',
    'description': 'Standalone backend design with custom navbar, sidebar, and home app grid. '
                   'Configure brand name, icon, and primary color from Settings.',
    'author': 'Shohjahon Obruyev',
    'depends': ['web', 'base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'oil_backend_theme/static/src/scss/primary_variables.scss',
        ],
        'web.assets_backend': [
            # Theme service — applies color CSS var before any component renders
            'oil_backend_theme/static/src/js/theme_config_service.js',
            # Layout templates and NavBar patch
            'oil_backend_theme/static/src/xml/menu_panels.xml',
            'oil_backend_theme/static/src/xml/nav_bar_panel.xml',
            'oil_backend_theme/static/src/xml/home_menus.xml',
            'oil_backend_theme/static/src/xml/side_bar_panel.xml',
            'oil_backend_theme/static/src/scss/backend_theme.scss',
            'oil_backend_theme/static/src/js/home_menus.js',
            'oil_backend_theme/static/src/js/search_apps.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
