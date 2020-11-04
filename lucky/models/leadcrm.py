# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError


import logging
_logger = logging.getLogger(__name__)


class lead (models.Model):
    _inherit = 'crm.lead'

    x_lead_status = fields.Selection([('New', 'New'),
                                        ('Contacted','Contacted'),
                                        ('Callback requested','Callback requested'),
                                        ('Wrong Info','Wrong Info'),
                                        ('Not Intersted','Not Intersted'),
                                        ('Not Contacted','Not Contacted'),
                                        ('Reached','Reached'),
                                        ('Un-Reached','Un-Reached'),
                                        ('Hang Up','Hang Up'),], string='Lead Status',default ='New')
    x_call_back_Date = fields.Datetime(string='Callback Date')
    

    #x_studio_lat = fields.Char(string="lat", required=False, index=False, track_visibility=False)
