# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'opemacademy.wizard'

    session_id = fields.Many2one('openacademy.session',
                                 string="Session", required=True)
    attendees_ids = fields.Many2many('res.partner', string="Attendees")