# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError
import datetime
import logging

class Post(models.Model):
    _name = "control.post"
    _description = "Control de publicaciones RRSS"


    name = fields.Char(string='Detalles')
    product_id = fields.Many2one('product.product', string='Producto', ondelete='restrict')
    date_publish = fields.Date(strin="Fecha Publicación")
