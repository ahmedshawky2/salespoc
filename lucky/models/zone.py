# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string

import logging
_logger = logging.getLogger(__name__)


class zone (models.Model):
    _name = 'x_zone'

    name = fields.Char(string="Zone Name", required=True, index=True, track_visibility='always')
    code = fields.Char(string="Zone Code", required=False, index=True, track_visibility='always')