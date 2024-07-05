
from odoo import models, fields, api
import json

class CalendlyHistoryModule(models.Model):
    _name = 'calendly.history'
    _description = 'Calendly History'
    _order = 'create_date desc'
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user, required = True,readonly=True)

    name = fields.Char(string='Description', readonly=True, required = True)
    model_name = fields.Char(string='Model',readonly=True)
    Start_Time = fields.Char(string='Start time', readonly=True,required = True)
    End_Time = fields.Char(string='End time', readonly=True, required = True)
    Invitee_Email = fields.Char(string='Invitee Email',readonly=True)
    Assignee_Email = fields.Char(string='Assignee Email' )
    Guest_Emails = fields.Char(string='Guest Emails')
    Contact_Number = fields.Char(string='Contact Number',readonly=True)
    Invitee_Timezone = fields.Char(string='Invitee timezone',readonly=True)
    Event_Type = fields.Char(string='Event type',readonly=True)
    Location = fields.Char(string='Location')
    Cancel_URL = fields.Char(string='Cancel URL',readonly=True)
    Reschedule_URL = fields.Char(string='Reschedule URL',readonly=True)

    timestamp = fields.Datetime(string='Created Time', default=fields.Datetime.now,  readonly=True, required = True)


