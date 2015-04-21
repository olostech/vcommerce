# -*- coding: utf-8 -*-
from django.db import models
from cadastro.empresa.models import Empresa

# Create your models here.
class Master(models.Model):
	"""docstring for ClassName"""
	class Meta:
		db_table = "master"

	id = models.AutoField(primary_key=True,verbose_name="Código", editable=False)
	empresa = models.ForeignKey(Empresa,verbose_name="Empresa")

from cadastro.unidade.models import Unidade

# Create your models here.
class Master_unidade(models.Model):
    unidade = models.ForeignKey(Unidade,verbose_name="Unidade",null=True)

from cadastro.empresa.models import Empresa

# Create your models here.
class Master_empresa(models.Model):
    empresa = models.ForeignKey(Empresa,verbose_name="Empresa",null=True)