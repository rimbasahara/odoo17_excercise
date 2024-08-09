from odoo import api, fields, models

class TrainStation(models.Model):
    _name = 'train.station'
    _description = 'Train Station'

    code = fields.Char(string='Code', required=True, tracking=True)
    name = fields.Char(string='Name', required=True, tracking=True)
    city = fields.Many2one('train.city', string='City', required=True)
    address = fields.Text(string='Address')