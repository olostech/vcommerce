# -*- coding: utf-8 -*-
from django.db import models
from vlib.vmodels import widgets
from django.contrib.auth.models import User
from cadastro.unidade.models import Unidade
from vlib.control.models import Master_empresa, ControleSincronizacao
from cadastro.localidade.pais.models import Pais
from cadastro.localidade.estado.models import Estado
from cadastro.localidade.cidade.models import Cidade
from cadastro.localidade.bairro.models import Bairro
import hashlib

TIPO_C = (('PF',u'Pessoa Física'),('PJ',u'Pessoa Jurídica'),)
SEXO_C = (('F','Feminino'),('M','Masculino'),)

# Create your models here.
class Funcionario(Master_empresa, ControleSincronizacao):
    user = models.ForeignKey(User, blank=True, null=True, editable=False)

    nome = models.CharField(max_length=255, verbose_name='Nome')
    usuario = models.CharField(max_length=255, verbose_name='Usuário')
    sexo = models.CharField(max_length=1,choices=SEXO_C, verbose_name='Sexo')
    dtnascimento = widgets.VDateField(verbose_name='Data de nascimento')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    senha = models.CharField(max_length=128, verbose_name='Senha')
    confsenha = models.CharField(max_length=128, verbose_name='Confirma Senha')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    numero = models.CharField(max_length=20, verbose_name='Número')
    complemento = models.CharField(max_length=255, null=True, blank=True, verbose_name='Complemento')
    cep = models.CharField(max_length=9,verbose_name='CEP', null=True)
    pais = models.ForeignKey(Pais,verbose_name="País")
    estado = models.ForeignKey(Estado,verbose_name='Estado')
    cidade = models.ForeignKey(Cidade,verbose_name='Cidade')
    bairro = models.ForeignKey(Bairro, blank=True, null=True, verbose_name='Bairro')
    dtadmissao = widgets.VDateField(verbose_name='Data de admissão',null=True,blank=True)
    dtdemissao = widgets.VDateField(verbose_name='Data de demissão',null=True,blank=True)
    pessoa = models.CharField(max_length=2,verbose_name='Tipo',choices=TIPO_C,default="PF")
#	unidadePadrao = models.CharField(verbose_name="Unidade padrão", QuerySet=Unidade.objects.all())
    unidade = models.ManyToManyField(Unidade, verbose_name="Unidades permitidas")

    class Meta:
        ordering = ['-id']
                
    def save(self):
        if not self.id:
            c = Funcionario.objects.filter(usuario=self.usuario).count()
            if c:
                raise UsuarioExistente
            usr = User.objects.filter(username=self.usuario)
            if usr:
                u = usr[0]
            else:
                u = User.objects.create_user(self.usuario, self.email, self.senha)
            u.save()
            self.user = u            
            #self.senha = hashlib.sha224(self.senha.encode('ascii')).hexdigest();
            #self.confsenha = hashlib.sha224(self.confsenha.encode('ascii')).hexdigest();
        else:
            self.user.username = self.usuario
            self.user.email = self.email
            self.user.set_password(self.senha)
            self.user.save()

        super(Funcionario, self).save()

    def __str__(self):
        return self.nome