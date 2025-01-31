# -*- coding: utf-8 -*- 
from django.db import models
from vlib.vmodels import widgets
from estoque.control.models import Master_moviest
from cadastro.fornecedor.models import Fornecedor

# Create your models here.
class Entrada(Master_moviest):
	class Meta:
		db_table = "entrada"
		verbose_name = "Entrada"
		verbose_name_plural = "Entradas"
		child_models = ['estoque.itemproduto.models.Itemproduto']
		ordering = ['-id']

	dtentrada = widgets.VDateField(verbose_name='Data de Entrada')
	fornecedor = models.ForeignKey(Fornecedor,verbose_name='Fornecedor', null=True)

	def __str__(self):
		return self.dtentrada