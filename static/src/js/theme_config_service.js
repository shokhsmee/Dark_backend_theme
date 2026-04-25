/** @odoo-module */

import { registry } from "@web/core/registry";

const oilThemeConfigService = {
    dependencies: ['orm'],

    async start(env, { orm }) {
        const [color, brandName, brandIcon] = await Promise.all([
            orm.call('ir.config_parameter', 'get_param', ['oil_theme.color']),
            orm.call('ir.config_parameter', 'get_param', ['oil_theme.brand_name']),
            orm.call('ir.config_parameter', 'get_param', ['oil_theme.brand_icon']),
        ]);

        const cfg = {
            color:     color     || '#FF6A00',
            brandName: brandName || 'Oil ERP',
            brandIcon: brandIcon ? ('bi-' + brandIcon) : 'bi-droplet-fill',
        };

        // Apply primary color as CSS variable before any component renders
        document.documentElement.style.setProperty('--oil-primary', cfg.color);

        return cfg;
    },
};

registry.category('services').add('oilThemeConfig', oilThemeConfigService);
