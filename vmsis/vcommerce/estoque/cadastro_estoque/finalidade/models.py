# -*- coding: utf-8 -*-
from django.db import models
from vlib.control.models import Master_empresa, ControleSincronizacao

# Create your models here.
class Finalidade(Master_empresa, ControleSincronizacao):
	class Meta:
		db_table = "finalidade"
		verbose_name = "Finalidade"
		verbose_name_plural = "Finalidades"
		ordering = ['descricao']

	descricao = models.CharField(max_length=150,verbose_name="Descrição",blank=True)

	def __str__(self):
		return self.descricao