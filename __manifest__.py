{
    'name': 'Dark Backend Theme',
    'version': '19.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Dark navy & orange backend theme — custom navbar, sidebar, app grid, configurable branding',
    'description': """
Dark Backend Theme for Odoo 19
==============================

A fully standalone backend theme with no business logic required.
Drop it on any Odoo 19 Community instance and get a professional
dark navy + industrial orange UI immediately.

Features
--------
- Dark navy navbar with orange accent border
- Icon-only 72px fixed sidebar with active state indicator
- Full-screen 5-column app grid home menu with background image
- Orange primary accent on buttons, checkboxes, icons, modals, statusbars
- League Spartan typography (Google Fonts)
- Bootstrap Icons for sidebar and app grid
- Configurable brand name, icon, and primary color from Settings
- Responsive: sidebar hides on mobile, grid collapses to 2-3 columns
- Pure UI layer: no models, no menus, no business logic

Configuration
-------------
Go to Settings > Dark Backend Theme to set:
- Brand Name: text shown next to the logo in the navbar
- Brand Icon: Bootstrap icon name (without bi- prefix), e.g. droplet-fill
- Primary Color: hex color code, e.g. #FF6A00

After saving, reload the page (F5) to apply changes.

CDN Note
--------
Bootstrap Icons and League Spartan are loaded from external CDNs.
For offline environments, host them locally and update the @import
URLs in static/src/scss/backend_theme.scss.
    """,
    'author': 'Shohjahon Obruyev',
    'website': 'https://github.com/shokhsmee/Dark_backend_theme',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'price': 9.99,
    'currency': 'USD',
    'depends': ['web', 'base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'oil_backend_theme/static/src/scss/primary_variables.scss',
        ],
        'web.assets_backend': [
            'oil_backend_theme/static/src/js/theme_config_service.js',
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
    'application': False,
    'auto_install': False,
}
