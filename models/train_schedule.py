from odoo import api, fields, models
from datetime import timedelta, datetime, date

class TrainSchedule(models.Model):
    _name = 'train.schedule'
    _description = 'Train Schedule'

    code = fields.Char(string='Code', readonly=True, default=lambda self: 'TRN/' + datetime.now().strftime('%Y/%m/%d/001'))
    origin = fields.Many2one('train.station', string='Origin', required=True)
    destination = fields.Many2one('train.station', string='Destination', required=True)
    schedule_time = fields.Datetime(string='Schedule Time', required=True)
    duration = fields.Float(string='Duration', required=True)
    arrival_time = fields.Datetime(string='Arrival Time', compute='_compute_arrival_time')
    train_id = fields.Many2one('train.train', string='Train', required=True)
    capacity = fields.Integer(string='Capacity', related='train_id.capacity')

    @api.depends('schedule_time', 'duration')
    def _compute_arrival_time(self):
        for rec in self:
            rec.arrival_time = rec.schedule_time + timedelta(hours=rec.duration)