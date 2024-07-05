# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import calendly_history_module
from . import iframe_model

class CRMLead(models.Model):
    _inherit = 'crm.lead'
    Lead_Source = fields.Char(string='Lead Source',readonly=True)

