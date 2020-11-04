# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import random

import logging
_logger = logging.getLogger(__name__)


class order (models.Model):
    _name = 'x_orders'
    x_name = fields.Char(string="Order#", required=False, index=True, track_visibility=False)
    x_studio_status = fields.Selection(string="Status", index=True, selection=[("New","New"),("Picked","Picked"),("Arrived","Arrived"),("Delivered","Delivered"),("Rejected","Rejected")], required=False , default="New")
    x_studio_customer_name = fields.Char(string="Customer Name", required=False, index=True, track_visibility=False)
    x_studio_customer_address = fields.Text(string="Customer Address", index=True, required=False)
    x_studio_driver = fields.Many2one(comodel_name="res.users",domain="[('x_is_driver','=',True)]", index=True, string="Driver", required=False)
    x_studio_phone = fields.Char(string="Phone", required=False, index=True, track_visibility=False)
    x_studio_picked_date = fields.Datetime(string="Picked Date", index=True, required=False)
    x_studio_arrived_date = fields.Datetime(string="Arrived  Date",index=True, required=False)
    x_studio_rejected_date = fields.Datetime(string="Rejected Date",index=True, required=False)
    x_studio_delivered_date_1 = fields.Datetime(string="Delivered Date",index=True, required=False)

    x_studio_lat = fields.Char(string="Driver Lat",related='x_studio_driver.x_studio_lat')
    x_studio_long = fields.Char(string="Driver Long",related='x_studio_driver.x_studio_long')
    x_studio_accuracy = fields.Char(string="Driver accuracy",related='x_studio_driver.x_studio_accuracy')

    x_studio_battery_level= fields.Char(string="Battery Level", related='x_studio_driver.x_studio_battery_level')
    #x_studio_GPS_TYPE = fields.Char(string="Battery Level", related='x_studio_driver.x_studio_GPS_TYPE')
    x_studio_prefered_time = fields.Char(string="Prefered Time", required=False, index=True, track_visibility=False)
    x_studio_comments = fields.Char(string="Comments", required=False, index=True, track_visibility=False)
    x_studio_priority = fields.Selection(string="Priority", index=True, selection=[("0","Normal"),("1","Low"),("2","High"),("3","Very High")], required=False)
    x_Order_Rand = fields.Char(compute='compute_Order_Rand', store=True, string='Order Key',index=True)
    x_customer_lat = fields.Float(string="Customer Lat", index=True, store=True)
    x_customer_long = fields.Float(string="Customer Long", index=True, store=True)
    x_qty = fields.Float(string="Quantity", index=True, store=True)
    x_price = fields.Float(string="Price", index=True, store=True)

    def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @api.one
    @api.depends('x_name')
    def compute_Order_Rand(self):
        if not self.x_Order_Rand:
            self.x_Order_Rand = order.id_generator()



    @api.onchange('x_studio_status')
    def sendsms(self):
        newstatus = self.x_studio_status;
        if (not newstatus) or (newstatus=="New"):
            return

        if newstatus == "Picked":
            self.x_studio_picked_date =datetime.datetime.now()
        elif newstatus == "Arrived":
            self.x_studio_arrived_date = datetime.datetime.now()
        elif newstatus == "Rejected":
            self.x_studio_rejected_date = datetime.datetime.now()
        elif newstatus == "Delivered":
            self.x_studio_delivered_date_1 = datetime.datetime.now()




