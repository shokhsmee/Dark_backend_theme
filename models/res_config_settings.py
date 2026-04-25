from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    oil_theme_color = fields.Char(
        string='Primary Color',
        config_parameter='oil_theme.color',
    )
    oil_brand_name = fields.Char(
        string='Brand Name',
        config_parameter='oil_theme.brand_name',
    )
    oil_brand_icon = fields.Char(
        string='Brand Icon',
        config_parameter='oil_theme.brand_icon',
        help='Bootstrap Icons class without the "bi-" prefix, e.g. droplet-fill, globe, gear-fill',
    )
