# -*- coding: utf-8 -*-

from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit="sale.order"

    payment_status = fields.Selection([('not_paid','Not Paid'),('partial_paid','Partial Paid'),('fully_paid','Full Paid'),('nothing','Invoice Not Created')],
                    string="Payment Status",compute="_compute_payment_status",
                    copy=False,store=True,readonly=True,
                    default="not_paid")

    @api.depends('invoice_ids.payment_state', 'invoice_ids.amount_residual')
    def _compute_payment_status(self):
        for rec in self:
            if rec.invoice_ids:
                full_paid = 0
                partial_paid = 0
                no_paid = 0
                for lines in rec.invoice_ids:
                    if lines.amount_residual == 0.0:
                        full_paid += 1
                    elif lines.amount_residual < lines.amount_total and lines.amount_residual > 0:
                        partial_paid += 1
                    else:
                        no_paid += 1
                if full_paid > 0 and partial_paid == 0 and no_paid == 0:
                    rec.payment_status = 'fully_paid'
                elif full_paid > 0 or full_paid == 0 and partial_paid > 0: 
                    rec.payment_status = 'partial_paid'
                else:
                    rec.payment_status = 'not_paid'
            else:
                rec.payment_status = 'nothing'
