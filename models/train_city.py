from odoo import api, fields, models

class TrainCity(models.Model):
    _name = 'train.city'
    _description = 'Studi Kasus'

    name = fields.Char(string='Nama', required=True, tracking=True)
    code = fields.Char(string='Code', required=True, tracking=True)