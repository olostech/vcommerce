# coding: utf-8
apps_on_menu = (
    {'app': 'cadastro', 'verbose_name' : 'Cadastro', 'imgmenu':'fa fa-cubes'},
    {'app': 'cadastro.almoxarifado', 'verbose_name' : 'Almoxarifado'},
    {'app': 'cadastro.almoxarifado.localizacao', 'verbose_name' : 'Localização', 'visible': False},
    {'app': 'cadastro.cliente', 'verbose_name' : 'Cliente'},
    {'app': 'cadastro.contato', 'verbose_name' : 'Contato', 'visible': False},
    {'app': 'cadastro.empresa', 'verbose_name' : 'Empresa'},
    {'app': 'cadastro.fornecedor', 'verbose_name' : 'Fornecedor'},
    {'app': 'cadastro.localidade', 'verbose_name' : 'Localidades' },
    {'app': 'cadastro.localidade.bairro', 'verbose_name' : 'Bairro'},
    {'app': 'cadastro.localidade.cidade', 'verbose_name' : 'Cidade'},
    {'app': 'cadastro.localidade.endereco', 'verbose_name' : 'Endereço', 'visible': False},
    {'app': 'cadastro.localidade.estado', 'verbose_name' : 'Estado'},
    {'app': 'cadastro.localidade.pais', 'verbose_name' : 'País'},
    {'app': 'cadastro.unimedida', 'verbose_name' : 'Unidade de Medida', 'visible': True},
    {'app': 'cadastro.produto', 'verbose_name' : 'Produto'},
    {'app': 'cadastro.unidade', 'verbose_name' : 'Unidade'},
    {'app': 'cadastro.funcionario', 'verbose_name' : 'Funcionário'},
    {'app': 'parametro', 'verbose_name' : 'Parâmetro', 'imgmenu':'fa fa-gear'},
    {'app': 'parametro.paramgeral', 'verbose_name' : 'Geral'},
    {'app': 'parametro.paramunidade', 'verbose_name' : 'Unidade'},
    {'app': 'parametro.controle_acesso', 'verbose_name' : 'Controle de Acesso'},
    {'app': 'vatualiza', 'verbose_name' : 'Atualização', 'visible': False},
    {'app': 'cadastro.centro_custo', 'verbose_name' : 'Centro de Custos'},    
    {'app': 'sincronizacao', 'verbose_name' : 'Centro de Custos', 'visisble': False},    
    

    # TELAS DA CONTABILIDADE
    # {'app': 'contabilidade', 'verbose_name' : 'Contabilidade', 'imgmenu' : 'glyphicon glyphicon-book'},
    # {'app': 'contabilidade.cadastro_contabil', 'verbose_name' : 'Cadastros Contábeis'},
    # {'app': 'contabilidade.cadastro_contabil.grupo_conta_contabil', 'verbose_name' : 'Contas contábeis - grupos',
    #     'visible' : True}, 
    # {'app': 'contabilidade.cadastro_contabil.tipo_escrituracao', 'verbose_name' : 'Tipos de escrituração', 'visible' : True},    
    # {'app': 'contabilidade.cadastro_contabil.historico_padrao', 'verbose_name' : 'Históricos padrões'},     
    # {'app': 'contabilidade.cadastro_contabil.plano_conta', 'verbose_name' : 'Plano de contas'},  
    # {'app': 'contabilidade.movimentacao_contabil', 'verbose_name' : 'Movimentações Contábeis'},
    # {'app': 'contabilidade.movimentacao_contabil.lancamento_contabil', 'verbose_name' : 'Lançamentos contábeis'},
    # {'app': 'contabilidade.movimentacao_contabil.lancamento_contabil_detalhe', 'verbose_name' : 'Partidas dos lançamentos', 
    #     'visible' : False},        

    # TELAS DO ESTOQUE
    {'app': 'estoque', 'verbose_name' : 'Estoque', 'imgmenu' : 'fa fa-th'},
    {'app': 'estoque.itemproduto', 'verbose_name' : 'Item', 'visible' : False},
    {'app': 'estoque.cadastro_estoque', 'verbose_name' : 'Cadastros Estoque'},
    {'app': 'estoque.cadastro_estoque.finalidade', 'verbose_name' : 'Finalidade'},      
    {'app': 'estoque.entrada', 'verbose_name' : 'Entrada'},
    {'app': 'estoque.saida', 'verbose_name' : 'Saída'},      
    {'app': 'estoque.posestoque', 'verbose_name' : 'Posição de Estoque', 'visible' : False},
    {'app': 'estoque.lote', 'verbose_name' : 'Lote', 'visible' : False},
    {'app': 'estoque.inventario', 'verbose_name' : 'Inventário'},
    {'app': 'estoque.inventario.iteminvent', 'verbose_name' : 'Item', 'visible' : False},
    {'app': 'estoque.transferencia', 'verbose_name' : 'Transferência'},
    {'app': 'estoque.transferencia.itemtransf', 'verbose_name' : 'Item', 'visible' : False},

   # TELAS DO PEDIDO
    {'app': 'pedido', 'verbose_name' : 'Pedido', 'imgmenu' : 'fa fa-building-o'},
    #{'app': 'pedido.frentecaixa', 'verbose_name' : 'Pedido'},
    {'app': 'pedido.itemreti', 'verbose_name' : 'Ajuste de Pedido'},
    {'app': 'pedido.cadastro_pedido', 'verbose_name' : 'Cadastros Pedido'},
    {'app': 'pedido.cadastro_pedido.mesa', 'verbose_name' : 'Mesa'},
    {'app': 'pedido.cadastro_pedido.agrupadicional', 'verbose_name' : 'Agrupamento de Adicionais'},
    #{'app': 'pedido.cadastro_pedido.cardapio', 'verbose_name' : 'Cardápio'},
    {'app': 'pedido.cadastro_pedido.categoria', 'verbose_name' : 'Categoria'},
    {'app': 'pedido.cadastro_pedido.itemcategoria', 'verbose_name' : 'Cardápio'},
    #{'app': 'pedido.cadastro_pedido.composicaoproduto', 'verbose_name' : 'Composição do Produto', 'visible' : False},
    {'app': 'pedido.cadastro_pedido.caixa', 'verbose_name' : 'Caixas'},
    {'app': 'pedido.aberfechcaixa', 'verbose_name' : 'Abertura e fechamento dos caixas', 
       'visible':False},
#    {'app': 'pedido.movcaixa', 'verbose_name' : 'Movimentações dos caixas'},    
#    {'app': 'pedido.fechcaixa', 'verbose_name' : 'Fechamento do caixa'},    
    #TELAS DO FINANCEIRO
     {'app': 'financeiro', 'verbose_name':'Financeiro', 'imgmenu':'fa fa-dollar'},
     {'app': 'financeiro.cartao_bandeira', 'verbose_name':'Bandeiras de Cartão'},
    # {'app': 'financeiro.banco', 'verbose_name': 'Banco', 'visible': False},
    # {'app': 'financeiro.conta', 'verbose_name': 'Conta'},
    # {'app': 'financeiro.mov_financeira','verbose_name': 'Transferencia Financeira'},
    # {'app': 'financeiro.contapagar', 'verbose_name' : 'Conta a Pagar'},
    # {'app': 'financeiro.contareceber', 'verbose_name' : 'Conta a Receber'},

)
