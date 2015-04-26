apps_on_menu = (
    {'app': 'cadastro', 'verbose_name' : 'Cadastro', 'imgmenu':'fa fa-cubes'},
    {'app': 'cadastro.almoxarifado', 'verbose_name' : 'Almoxarifado'},
    {'app': 'cadastro.cliente', 'verbose_name' : 'Cliente'},
    {'app': 'cadastro.contato', 'verbose_name' : 'Contato', 'visible': False},
    {'app': 'cadastro.empresa', 'verbose_name' : 'Empresa'},
    {'app': 'cadastro.fornecedor', 'verbose_name' : 'Fornecedor'},
    {'app': 'cadastro.banco', 'verbose_name': 'Banco', 'visible': False},
    {'app': 'cadastro.conta', 'verbose_name': 'Conta'},
    {'app': 'cadastro.localidade', 'verbose_name' : 'Localidades' },
    {'app': 'cadastro.localidade.bairro', 'verbose_name' : 'Bairro'},
    {'app': 'cadastro.localidade.cidade', 'verbose_name' : 'Cidade'},
    {'app': 'cadastro.localidade.endereco', 'verbose_name' : 'Endereço', 'visible': False},
    {'app': 'cadastro.localidade.estado', 'verbose_name' : 'Estado'},
    {'app': 'cadastro.localidade.pais', 'verbose_name' : 'Países'},
    {'app': 'cadastro.produto', 'verbose_name' : 'Produto'},
    {'app': 'cadastro.produto.item', 'verbose_name' : 'Produto'},
    {'app': 'cadastro.produto.localizacao', 'verbose_name' : 'Localização', 'visible': False},
    {'app': 'cadastro.produto.unimedida', 'verbose_name' : 'Unidade de Medida'},
    {'app': 'cadastro.unidade', 'verbose_name' : 'Unidade'},
    {'app': 'cadastro.funcionario', 'verbose_name' : 'Funcionário'},
    {'app': 'parametro', 'verbose_name' : 'Parâmetro', 'imgmenu':'fa fa-gear'},
    {'app': 'parametro.paramgeral', 'verbose_name' : 'Geral'},
    {'app': 'parametro.paramunidade', 'verbose_name' : 'Unidade'},
    {'app': 'vatualiza', 'verbose_name' : 'Atualização', 'visible': False},
    {'app': 'cadastro.centro_custo', 'verbose_name' : 'Centro de Custos'},    
    
    # TELAS DA CONTABILIDADE
    {'app': 'contabilidade', 'verbose_name' : 'Contabilidade', 'imgmenu' : 'glyphicon glyphicon-book'},
    {'app': 'contabilidade.cadastro_contabil', 'verbose_name' : 'Cadastros Contábeis'},
    {'app': 'contabilidade.cadastro_contabil.grupo_conta_contabil', 'verbose_name' : 'Contas contábeis - grupos',
        'visible' : True}, 
    {'app': 'contabilidade.cadastro_contabil.tipo_escrituracao', 'verbose_name' : 'Tipos de escrituração', 'visible' : True},    
    {'app': 'contabilidade.cadastro_contabil.historico_padrao', 'verbose_name' : 'Históricos padrões'},     
    {'app': 'contabilidade.cadastro_contabil.plano_conta', 'verbose_name' : 'Plano de contas'},  
    {'app': 'contabilidade.movimentacao_contabil', 'verbose_name' : 'Movimentações Contábeis'},
    {'app': 'contabilidade.movimentacao_contabil.lancamento_contabil', 'verbose_name' : 'Lançamentos contábeis'},
    {'app': 'contabilidade.movimentacao_contabil.lancamento_contabil_detalhe', 'verbose_name' : 'Partidas dos lançamentos', 
        'visible' : False},        

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

)
