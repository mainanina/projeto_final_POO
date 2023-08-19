from classes.clientes import Clientes
from classes.medicamentos import Medicamentos
from classes.medicamentos_fitoterapicos import MedicamentosFitoterapicos
from classes.medicamentos_quimioterapicos import MedicamentosQuimioterapicos
from classes.vendas import Vendas

def criar_relatorio_cliente():
    print("\nRELATÓRIO: Listagem de Cientes")
    print("-----------------------------------------------------")
    lista_clientes = sorted(Clientes.cadastro_clientes, key=lambda cliente: cliente.nome)
    for cliente in lista_clientes:
        print(cliente)

def criar_relatorio_medicamentos():
    print("\nRELATÓRIO: Listagem de Medicamentos")
    print("-----------------------------------------------------")
    lista_med = sorted(Medicamentos.cadastro_medicamentos, key=lambda med: med.nome)
    for med in lista_med:
        print(med)

def criar_relatorio_med_especifico(classe: str):
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
    lista_vendas = Vendas.vendas_dia
    print("RELATÓRIO: Atendimentos do dia")
    print("-----------------------------------------------------")
    remedio_mais, unidades_mais_vendido, valor_mais_vendido = obter_mais_vendido(lista_vendas)
    qtdd_dia = calcular_clientes_atendidos(lista_vendas)
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
            Valor total: {valor_mais_vendido}
        Quantidade de pessoas atendidas: {qtdd_dia}
        Quimioterápicos vendidos no dia:
            Quantidade: {vendas_quimio["unidades"]}
            Valor total: {vendas_quimio["valor"]}
        Fitoterápicos vendidos no dia:
            Quantidade: {vendas_fito["unidades"]}
            Valor total: {vendas_fito['valor']}
        ''')
    
def obter_mais_vendido(lista: [Vendas]):
    vendas_dia = {}
    for venda in lista:
        for produto, valor in venda.produtos.items():
            if produto not in vendas_dia.keys():
                vendas_dia[produto] = {"quantidade": valor['unidades'], "valor": valor['unidades'] * valor['valor_unit']}
            else: 
                vendas_dia[produto]["quantidade"] += valor['unidades']
                vendas_dia[produto]["valor"] += valor['unidades'] * valor['valor_unit']
    item_mais_vendido = max(vendas_dia, key=lambda item: vendas_dia[item]["quantidade"], default=0)
    if item_mais_vendido != 0:
        unidades_mais_vendido = vendas_dia[item_mais_vendido]["quantidade"]
        valor_mais_vendido = vendas_dia[item_mais_vendido]["valor"]
    else:
        item_mais_vendido = "Não houve vendas no dia"
        unidades_mais_vendido = 0
        valor_mais_vendido = 0
    return item_mais_vendido, unidades_mais_vendido, valor_mais_vendido

def calcular_clientes_atendidos(lista: [Vendas]):
    clientes = set([venda.cliente.nome for venda in lista])
    return len(clientes)
