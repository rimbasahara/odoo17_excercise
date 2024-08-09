from odoo import api, fields, models

class TrainTrain(models.Model):
    _name = 'train.train'
    _description = 'Train'

    name = fields.Char(string='Name', required=True, tracking=True)
    code = fields.Char(string='Code', required=True, tracking=True)
    capacity = fields.Integer(string='Capacity', required=True)
    state = fields.Selection([('ready', 'Ready'), ('not_ready', 'Not Ready'), ('maintenance', 'Maintenance')], default='ready')
    active = fields.Boolean(string='Active', default=True)
    schedule_line = fields.One2many('train.schedule', 'train_id', string='Schedule Line')