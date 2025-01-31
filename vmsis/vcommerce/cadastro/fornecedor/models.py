# -*- coding: utf-8 -*-
from django.db import models
from vlib.control.models import Master_endereco, EnderecoGenerico, ControleSincronizacao


choice_tipo_jfo = (('J','Jurídica'),
	('F','Física'),
	('O','Outros'))

# Create your models here.
class Fornecedor(Master_endereco, EnderecoGenerico, ControleSincronizacao):
    class Meta:
        db_table = "fornecedor"
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['nmfornecedor']
        child_models = ['cadastro.localidade.endereco.models.Endereco',
                        'cadastro.contato.models.Contato']

    identificador = models.CharField(max_length=1,verbose_name="Tipo",choices=choice_tipo_jfo)
    nrinscjurd = models.CharField(max_length=20,verbose_name="Inscrição Jurídica")
    nmfornecedor = models.CharField(max_length=250,verbose_name="Nome",unique=True)
    telcel = models.CharField(max_length=15,verbose_name="Telefone celular", blank=True, 
        null=True)
    telfixo = models.CharField(max_length=15,verbose_name="Telefone fixo",blank=True,
        null=True)    


    def __str__(self):
        return self.nmfornecedor