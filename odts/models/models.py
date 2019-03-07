# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VistaPrincipal(models.Model):
    _name = 'autos'

    nombre = fields.Char(string='Nombre del auto', help='Introduce el nombre del vehiculo')
    marca = fields.Many2one('autos.marca', string='Marca', help='Selecciona la marca del vehiculo') # Este campo nos sirve para crear una relacion con otra tabla
    modelo = fields.Char(string='Modelo')
    year_fabricante = fields.date(string='Fecha de fabicación')
    color = fields.Char(string=('Color'))
    kilomet = fields.Integer(string='Kilometraje')
    garanty = fields.Boolean(string='Garantia')
    transmision = fields.Selection([('1','Automatico'),('2','Standart'),('3','Surtido Rico')]string='Tipo de transmisión')
    puertas = fields.Integer(string='No. de Puertas')
    pasajeros = fields.Float(string='No. de Pasajeros')
    litros = fields.Float(string='Litros (Motor)')
    cilindros = fields.Integer(string='Cilindros')
    combustible = fields.Selection([('1','Electrico'),('2','Magna'),('3','Premium'),('4','Diesel')]string='Combustible')
    picture = fields.Binary()

class MarcasAutos(models.Model):
	_name = 'autos.marca'

	name = fields.Char(string='Nombre de la Marca')
