# -*- coding: utf-8 -*-
import json

from odoo import models, fields, api


class AccountMove(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _inherit = "account.move"

    ob1 = fields.Monetary(string='Paid', store=True, readonly=True, tracking=True, compute='_compute_ob1')
    ob2 = fields.Monetary(string='total paid', store=True, readonly=True, tracking=True, compute='_compute_ob2')

    # ---------------------------------------- Action Methods -------------------------------------
    # =======================================================================
    @api.depends('tax_totals_json','amount_total','amount_residual')
    def _compute_ob1(self):
        for move in self:
            self.ob1 = abs(move.amount_total - move.amount_residual)
    @api.depends('tax_totals_json','amount_tax','ob1')
    def _compute_ob2(self):
        for move in self:
            if move.ob1==0.0:
                self.ob2 = abs(move.ob1)
            else:
                self.ob2 = move.ob1+move.amount_tax
                # self.amount_residual=move.amount_total-move.ob2



