from vlib import view_lib
from django.core.exceptions import ValidationError
from fluxocaixa.contareceber.models import ContaReceber
from datetime import *

import sys

class FormContaReceber(view_lib.StandardFormGrid):
    class Meta:
        model = ContaReceber

    def save(self, commit = False):

        def InserirDados(self, p_dtvencimento):
            cap = ContaReceber()
            setattr(cap, 'cdempresa', self.cdempresa)
            setattr(cap, 'nrinscjurdUnid', self.nrinscjurdUnid)
            setattr(cap, 'idformapagamento', self.idformapagamento)
            setattr(cap, 'dscontareceber', self.dscontareceber)
            setattr(cap, 'nrinscjurdForn', self.nrinscjurdForn)
            setattr(cap, 'vrcontareceber', self.vrcontareceber)
            setattr(cap, 'dtvencimento', p_dtvencimento)
            setattr(cap, 'idrepetir', self.idrepetir)
            setattr(cap, 'dtfinal', self.dtfinal)
            setattr(cap, 'idstatus', "1")
            setattr(cap, 'idorigem', self.id)

            try:
                cap.full_clean()
            except ValidationError as e:
                raise
            else:
                cap.save()

        instance = super(FormContaReceber, self).save(commit=True)

        if instance.idrepetir != "1":
            if (instance.idorigem == "") or (instance.idorigem is None):
                dtDifeDatas = instance.dtfinal - instance.dtvencimento

                if instance.idrepetir == "2":
                    qtdlanc = dtDifeDatas.days
                    for x in range(qtdlanc):
                        dtvencimento = instance.dtvencimento + timedelta(days=(x + 1))
                        InserirDados(instance, dtvencimento)

                if instance.idrepetir == "3":
                    qtdlanc = (int)(dtDifeDatas.days / 7)
                    for x in range(qtdlanc):
                        dtvencimento = instance.dtvencimento + timedelta(days=(x + 7))
                        InserirDados(instance, dtvencimento)

                if instance.idrepetir == "4":
                    qtdlanc = (int)(dtDifeDatas.days / 15)
                    for x in range(qtdlanc):
                        dtvencimento = instance.dtvencimento + timedelta(days=(x + 15))
                        InserirDados(instance, dtvencimento)

                if instance.idrepetir == "5":
                    qtdlanc = (int)(dtDifeDatas.days / 30)
                    for x in range(qtdlanc):
                        dtvencimento = instance.dtvencimento + timedelta(days=(x + 30))
                        InserirDados(instance, dtvencimento)

                if instance.idrepetir == "6":
                    qtdlanc = (int)(dtDifeDatas.days / 90)
                    for x in range(qtdlanc):
                        dtvencimento = instance.dtvencimento + timedelta(days=(x + 90))
                        InserirDados(instance, dtvencimento)

                if instance.idrepetir == "7":
                    qtdlanc = (int)(dtDifeDatas.days / 365)
                    for x in range(qtdlanc):
                        dtvencimento = instance.dtvencimento + timedelta(days=(x + 365))
                        InserirDados(instance, dtvencimento)

# Create your views here.
class ViewContaReceber(view_lib.ViewCreate):
    form_class = FormContaReceber