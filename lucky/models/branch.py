# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string

import logging
_logger = logging.getLogger(__name__)


class branch (models.Model):
    _name = 'x_branch'

    name = fields.Char(string="Branch Name", required=True, index=True, track_visibility=False)
    x_code = fields.Char(string="Branch Code", required=False, index=True, track_visibility=False)
    x_branch_lat = fields.Float(string="Branch Lat", index=True, store=True, track_visibility=False)
    x_branch_long = fields.Float(string="Branch Long", index=True, store=True, track_visibility=False)
    x_branch_address = fields.Text(string="Branch Address", index=True, store=True, track_visibility=False)