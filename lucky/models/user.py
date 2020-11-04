# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError


import logging
_logger = logging.getLogger(__name__)


class user (models.Model):
    _inherit = 'res.users'

    x_studio_lat = fields.Char(string="lat", required=False, index=False, track_visibility=False)
    x_studio_long = fields.Char(string="long", required=False, index=False, track_visibility=False)
    x_studio_accuracy = fields.Char(string="Accuracy", required=False)
    x_studio_battery_level = fields.Char(string="Battery Level", required=False)
    #x_studio_GPS_TYPE= fields.Char(string="GPS Type", required=False)
    x_is_driver = fields.Boolean(string="Is driver", required=False, index=True, track_visibility=False)
    x_driver_car_type = fields.Many2one(comodel_name="x_car_type", index=True, string="Driver Car Type", required=False, track_visibility=False)
