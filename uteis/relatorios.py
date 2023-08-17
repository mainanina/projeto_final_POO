from classes import Clientes, Medicamentos, MedicamentosQuimioterapicos, MedicamentosFitoterapicos, Vendas

def criar_relatorio_cliente():
    print("RELATÓRIO: Listagem de Cientes")
    print("-----------------------------------------------------")
    lista_clientes = (Clientes.cadastro_clientes).sort()
    for cliente in lista_clientes:
        print(cliente)
        print("--------------------------------------------")

def criar_relatorio_medicamentos():
    print("RELATÓRIO: Listagem de Medicamentos")
    print("-----------------------------------------------------")
    lista_med = (Medicamentos.cadastro_medicamentos).sort()
    for med in lista_med:
        print(med)
        print("--------------------------------------------")

def criar_relatorio_med_especifico(classe: str):
    lista_med = (Medicamentos.cadastro_medicamentos).sort()
    selecionados = []
    if classe == "q":
        selecionados = [med for med in lista_med if isinstance(med, MedicamentosQuimioterapicos)]
        print("RELATÓRIO: Listagem de Quimioterápicos")
        print("-----------------------------------------------------")
    elif classe == "f":
        selecionados = [med for med in lista_med if isinstance(med, MedicamentosFitoterapicos)]
        print("RELATÓRIO: Listagem de Fitoterápicos")
        print("-----------------------------------------------------")
    for med in selecionados:
        print(med)

def criar_relatorio_dia():
    lista_vendas = Vendas.vendas_dia
    print("RELATÓRIO: Atendimentos do dia")
    print("-----------------------------------------------------")
    remedio_mais, unidades_mais_vendido, valor_mais_vendido = obter_mais_vendido(lista_vendas)
    qttd_dia = calcular_clientes_atendidos(lista_vendas)
    vendas_quimio = [venda for venda in lista_vendas if isinstance(venda.prod_vend, MedicamentosQuimioterapicos)]
    vendas_fito = [venda for venda in lista_vendas if isinstance(venda.prod_vend, MedicamentosFitoterapicos)]
    qtt_quimio, valor_quimio = calcular_vendas(vendas_quimio)
    qtt_fito, valor_fito = calcular_vendas(vendas_fito)
    print(f'''
        Medicamento mais vendido no dia: 
            {remedio_mais} -> {unidades_mais_vendido} unidades
            Valor total: {valor_mais_vendido}
        Quantidade de pessoas atendidas: {qttd_dia}
        Quimioterápicos vendidos no dia:
            Quantidade: {qtt_quimio}
            Valor total: {valor_quimio}
        Fitoterápicos vendidos no dia:
            Quantidade: {qtt_fito}
            Valor total: {valor_fito}
        ''')
    
def obter_mais_vendido(lista: [Vendas]):
    vendas_dia = {}
    for venda in lista:
        for produto, qttd in venda.prod_vend:
            if produto.nome not in vendas_dia.keys():
                vendas_dia[produto.nome] = {"quantidade": qttd, "valor": qttd * produto.valor}
            else: 
                vendas_dia[produto.nome]["quantidade"] += qttd
                vendas_dia[produto.nome]["valor"] += qttd * produto.valor
    item_mais_vendido = max(vendas_dia, key=lambda item: vendas_dia[item]["quantidade"])
    unidades_mais_vendido = vendas_dia[item_mais_vendido]["quantidade"]
    valor_mais_vendido = vendas_dia[item_mais_vendido]["valor"]
    return item_mais_vendido, unidades_mais_vendido, valor_mais_vendido

def calcular_clientes_atendidos(lista: [Vendas]):
    clientes = set([venda.cliente.nome for venda in lista])
    return len(clientes)

def calcular_vendas(lista: [Vendas]):
    soma_unidades = 0
    valor_total = 0
    for venda in lista:
        for produto, qttd in venda.prod_venda:
            soma_unidades += qttd
            valor_total += (qttd*produto.valor)
    return soma_unidades, valor_total