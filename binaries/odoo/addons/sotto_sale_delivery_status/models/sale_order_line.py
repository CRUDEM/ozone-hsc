# -*- coding: utf-8 -*-

from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit="sale.order"

    delivery_status = fields.Selection([('no_delivery','Not Delivered'),('partial_delivery','Partial Delivered'),('full_delivery','Full Delivered'),('nothing','Nothing to Deliver')],
                    string="Delivery Status",compute="_compute_delivery_status",
                    copy=False,store=True,readonly=True,
                    default="nothing")

    @api.depends('state', 'order_line.qty_delivered')
    def _compute_delivery_status(self):
        for rec in self:
            if rec.picking_ids:
                full_delivery = 0
                partial_delivery = 0
                no_delivery = 0
                storable = rec.mapped('order_line').filtered(lambda x:x.product_id.type != 'service')
                service =  rec.mapped('order_line').filtered(lambda x:x.product_id.type == 'service')
                for lines in storable:
                    if lines.product_uom_qty == lines.qty_delivered:
                        full_delivery += 1
                    elif lines.qty_delivered < lines.product_uom_qty and lines.qty_delivered > 0:
                        partial_delivery += 1
                    else:
                        no_delivery += 1
                print("\n\n\n",full_delivery)
                print("\n\n\n",partial_delivery)
                print("\\n\n\n",no_delivery)
                if full_delivery > 0 and partial_delivery == 0 and no_delivery == 0:
                    rec.delivery_status = 'full_delivery'
                elif full_delivery > 0 or full_delivery == 0 and partial_delivery > 0: 
                    rec.delivery_status = 'partial_delivery'
                else:
                    rec.delivery_status = 'no_delivery'
                if storable and service and rec.state == 'sale':
                    rec.delivery_status = 'delivered'
            else:
                rec.delivery_status = 'nothing'
