# -*- coding: utf-8 -*-
class Edades:
	def mensaje(self, edad):
		if edad < 0:
			return 'no existes'
		if edad < 13 and edad > 0:
			return u'Eres un niño'
		if edad <18 and edad > 13:
			return 'Eres adolescente'
		if edad < 65 and edad > 18:
			return 'Eres adulto'
		if edad < 120 and edad > 65:
			return 'Eres adulto mayor'
		if edad > 120 and edad < 999:
			return 'Eres Mumm-Ra'
		if edad > 1000 and edad < 1200:
			return 'Eres una momia'

			#
		