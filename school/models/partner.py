from odoo import models, fields, api, _


class Partner(models.Model):

    _inherit = "res.partner"

    state = fields.Selection([('a', 'Active'), ('i', 'Inactive')], "STATE", select=True)
    bdate = fields.Date("Birth Date")

    @api.multi
    def change_active(self):
        self.state = 'a'
        self.active = 1

    @api.multi
    def change_inactive(self):
        self.state = 'i'
        self.active  = 0

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    b_date = fields.Date('Customer B-day')

    # @api.multi
    # @api.onchange('partner_id')
    # def onchange_partner_id(self):
    #     print "======>",dir(self)
    #     if self.partner_id.bdate:
    #         self.b_date = self.partner_id.bdate
    #     res = super(SaleOrder,self).onchange_partner_id()
    #     return res

    # @api.multi
    # @api.onchange('partner_id')
    # def onchange_partner_id(self):
    #     """
    #     Update the following fields when the partner is changed:
    #     - Pricelist
    #     - Payment term
    #     - Invoice address
    #     - Delivery address
    #     """
    #     if not self.partner_id:
    #         self.update({
    #             'partner_invoice_id': False,
    #             'partner_shipping_id': False,
    #             'payment_term_id': False,
    #             'fiscal_position_id': False,
    #         })
    #         return
    #
    #     addr = self.partner_id.address_get(['delivery', 'invoice'])
    #     values = {
    #         'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
    #         'payment_term_id': self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
    #         'partner_invoice_id': addr['invoice'],
    #         'partner_shipping_id': addr['delivery'],
    #     }
    #     if self.env.user.company_id.sale_note:
    #         values['note'] = self.with_context(lang=self.partner_id.lang).env.user.company_id.sale_note
    #
    #     if self.partner_id.user_id:
    #         values['user_id'] = self.partner_id.user_id.id
    #     if self.partner_id.team_id:
    #         values['team_id'] = self.partner_id.team_id.id
    #     self.update(values)


