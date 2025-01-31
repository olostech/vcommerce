# -*- coding: utf-8 -*-
from django.db import models
from vlib.vmodels import widgets
from estoque.control.models import Master_moviest
from cadastro.cliente.models import Cliente
from estoque.cadastro_estoque.finalidade.models import Finalidade

choice_tipo = (('R','Retirada'),
	('P','Perda'))

# Create your models here.
class Saida(Master_moviest):
    class Meta:
        db_table = "saida"
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
        child_models = ['estoque.itemproduto.models.Itemproduto']
        ordering = ['-id']

    dtsaida = widgets.VDateField(verbose_name='Data de saída')
    cliente = models.ForeignKey(Cliente,verbose_name='Cliente')
    finalidade = models.ForeignKey(Finalidade,verbose_name='Finalidade',null=True,blank=True)
    idtipo = models.CharField(max_length=1,verbose_name="Tipo de Saída",choices=choice_tipo)

    def __str__(self):
        return self.dtsaida