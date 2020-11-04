# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError


import logging
_logger = logging.getLogger(__name__)


class user (models.TransientModel):
    _inherit = 'crm.lead.lost'

    x_user_has_anther_Account = fields.Selection([('Y', 'Yes'),('N','No')], string='User has Another Account')
    x_use_lucky_info = fields.Selection([('Y', 'Yes'),('N','No')], string='User understand That he could use lucky without deal')
    x_lost_reasons = fields.Selection([('Active Subscription with competitor', 'Active Subscription with competitor'),
                                    ('Bad Experience','Bad Experience'),
                                    ('Desired brands are not available','Desired brands are not available'),
                                    ('Dsquares/Lucky employess','Dsquares/Lucky employess'),
                                    ('Expensive','Expensive')], string='Not Interested Reason' )
    x_resanble_price = fields.Integer(string='Reasonable price recommended')
    x_another_reason = fields.Text(string='Another Reason')

    #x_studio_lat = fields.Char(string="lat", required=False, index=False, track_visibility=False)
