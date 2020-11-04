# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string

import logging
_logger = logging.getLogger(__name__)


class car_type (models.Model):
    _name = 'x_car_type'

    name = fields.Char(string="Car Type", required=True, index=True, track_visibility='always')