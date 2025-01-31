# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from vlib.view_lib import CrudView
from pedido.frentecaixa.models import Pedido
from pedido.frentecaixa.views import ViewFrentecaixaCreate, ViewFrentecaixaUpdate


Crud = CrudView(Pedido)

urlpatterns = Crud.AsUrl(MediaFilesInsert = ['js/pedido.js'],MediaFilesUpdate = ['js/pedido.js'],ClassCreate = ViewFrentecaixaCreate,ClassUpdate = ViewFrentecaixaUpdate,GridFields  = ('idtipopedido','vrpedido'))