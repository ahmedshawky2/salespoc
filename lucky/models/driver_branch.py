# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string

import logging
_logger = logging.getLogger(__name__)


class driver_branch (models.Model):
    _name = 'x_driver_branch'

    x_driver_id = fields.Many2one(comodel_name="res.users", string="Driver Name", required=False, index=True, track_visibility='always')
    x_branch_id = fields.Many2one(comodel_name="x_branch", string="Branch Name", required=False, index=True, track_visibility='always')