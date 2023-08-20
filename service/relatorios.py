from classes.clientes import Clientes
from classes.medicamentos import Medicamentos
from classes.medicamentos_fitoterapicos import MedicamentosFitoterapicos
from classes.medicamentos_quimioterapicos import MedicamentosQuimioterapicos
from classes.vendas import Vendas


def criar_relatorio_cliente():
    '''
    Cria relatório impresso no terminal com todos os clientes cadastrados em ordem alfabética
    '''
    print("\nRELATÓRIO: Listagem de Cientes")
    print("-----------------------------------------------------")
    lista_clientes = sorted(Clientes.cadastro_clientes, key=lambda cliente: cliente.nome)
    for cliente in lista_clientes:
        print(cliente)


def criar_relatorio_medicamentos():
    '''
    Cria relatório impresso no terminal com todos os medicamentos cadastrados em ordem alfabética
    '''
    print("\nRELATÓRIO: Listagem de Medicamentos")
    print("-----------------------------------------------------")
    lista_med = sorted(Medicamentos.cadastro_medicamentos, key=lambda med: med.nome)
    for med in lista_med:
        print(med)


def criar_relatorio_med_especifico(classe: str):
    '''
    Recebe uma strinq "q" ou "f" e cria relatório impresso no terminal 
    com medicamentos específicos de uma classe (q = quimioterápicos, f=fitoterápicos)
    '''
    lista_med = sorted(Medicamentos.cadastro_medicamentos, key=lambda med: med.nome)
    selecionados = []
    if classe == "q":
        selecionados = [med for med in lista_med if isinstance(med, MedicamentosQuimioterapicos)]
        print("\nRELATÓRIO: Listagem de Quimioterápicos")
        print("-----------------------------------------------------")
    elif classe == "f":
        selecionados = [med for med in lista_med if isinstance(med, MedicamentosFitoterapicos)]
        print("\nRELATÓRIO: Listagem de Fitoterápicos")
        print("-----------------------------------------------------")
    for med in selecionados:
        print(med)


def criar_relatorio_dia():
    '''
    Cria relatório impresso no terminal com as vendas realizadas desde o início do sistema até sua finalização, 
    incluindo medicamento mais vendido (número de unidades e valor), número de clientes distintos atendidos,
    quimioterápios e fitoterápicos vendicos com número de unidades e valor.
    '''
    lista_vendas = Vendas.vendas_dia
    print("RELATÓRIO: Atendimentos do dia")
    print("-----------------------------------------------------")
    remedio_mais, unidades_mais_vendido, valor_mais_vendido = obter_mais_vendido(lista_vendas)
    qtdd_dia = len(set([venda.cliente.nome for venda in lista_vendas]))
    vendas_quimio = {'unidades': 0, 'valor': 0}
    vendas_fito = {'unidades': 0, 'valor': 0}
    for venda in lista_vendas:
        for item, valor in venda.produtos.items():
            if valor['categoria'] == 'f':
                vendas_fito['unidades'] += valor['unidades']
                vendas_fito['valor'] += (valor['unidades']* valor['valor_unit'])
            elif valor['categoria'] == 'q':
                vendas_quimio['unidades'] += valor['unidades']
                vendas_quimio['valor'] += (valor['unidades']* valor['valor_unit'])
    print(f'''
        Medicamento mais vendido no dia: 
            {remedio_mais} -> {unidades_mais_vendido} unidades
            Valor total: {round(valor_mais_vendido, 2)}
        Quantidade de pessoas atendidas: {qtdd_dia}
        Quimioterápicos vendidos no dia:
            Quantidade: {vendas_quimio["unidades"]}
            Valor total: {round(vendas_quimio["valor"], 2)}
        Fitoterápicos vendidos no dia:
            Quantidade: {vendas_fito["unidades"]}
            Valor total: {round(vendas_fito['valor'], 2)}
        ''')
    

def obter_mais_vendido(lista: [Vendas]):
    '''
    Recebe uma lista de objetos do tipo Vendas e retorna qual o item mais vendido do dia, o número de unidades
    vendidas desse item e o valor total.
    Se não houver vendas na lista, retorna a mensagem de que não houve vendas no dia.
    '''
    if len(lista) != 0:
        vendas_dia = {}
        for venda in lista:
            for produto, valor in venda.produtos.items():
                if produto not in vendas_dia.keys():
                    vendas_dia[produto] = {"quantidade": valor['unidades'], "valor": valor['unidades'] * valor['valor_unit']}
                else: 
                    vendas_dia[produto]["quantidade"] += valor['unidades']
                    vendas_dia[produto]["valor"] += valor['unidades'] * valor['valor_unit']
        item_mais_vendido = max(vendas_dia, key=lambda item: vendas_dia[item]["quantidade"], default=0)
        unidades_mais_vendido = vendas_dia[item_mais_vendido]["quantidade"]
        valor_mais_vendido = vendas_dia[item_mais_vendido]["valor"]
    else:
        item_mais_vendido = "Não houve vendas no dia"
        unidades_mais_vendido = 0
        valor_mais_vendido = 0
    return item_mais_vendido, unidades_mais_vendido, valor_mais_vendido
