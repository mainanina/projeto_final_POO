from classes import Clientes, Medicamentos, MedicamentosQuimioterapicos, MedicamentosFitoterapicos

def criar_relatorio_cliente():
    print("RELATÓRIO: Listagem de Cientes")
    print("-----------------------------------------------------")
    lista_clientes = (Clientes.cadastro_clientes).sort()
    for cliente in lista_clientes:
        print(f"""
        CPF: {cliente.cpf}
        Nome: {cliente.nome}
        Data de Nascimento: {cliente.dn}
        --------------------------------------------\n
        """)

def criar_relatorio_medicamentos():
    print("RELATÓRIO: Listagem de Medicamentos")
    print("-----------------------------------------------------")
    lista_med = (Medicamentos.cadastro_medicamentos).sort()
    for med in lista_med:
        print(f"""
        Nome: {med.nome}
        Principal Composto: {med.pp_composto}
        Laboratório: {med.laboratorio}
        Descrição: {med.descricao}
        --------------------------------------------\n
        """)

def criar_relatorio_med_especifico(classe: str):
    lista_med = (Medicamentos.cadastro_medicamentos).sort()
    quimio = []
    fito = []
    if classe == q:
        for med in lista_med:
            if isinstance(med, MedicamentosQuimioterapicos):
                quimio.append(med)
        print("RELATÓRIO: Listagem de Quimioterápicos")
        print("-----------------------------------------------------")
        for q in quimio:
            print(f"""
            Nome: {q.nome}
            Principal Composto: {q.pp_composto}
            Laboratório: {q.laboratorio}
            Descrição: {q.descricao}
            Precisa de receita? {q.precisa_receita}
            --------------------------------------------\n
            """)

