from odoo import api, models, fields

class Warehouse(models.Model):
    _inherit = "stock.warehouse"

    @api.model
    def create(self, vals):
        
        warehouse = super(models.Model, self).create(vals)

        # update partner data if partner assigned
        if vals.get('partner_id'):
            self._update_partner_data(vals['partner_id'], vals.get('company_id'))

        self._check_multiwarehouse_group()

        return warehouse
