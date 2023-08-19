from datetime import datetime
from classes.clientes import Clientes
from classes.medicamentos import Medicamentos
from classes.medicamentos_fitoterapicos import MedicamentosFitoterapicos
from classes.medicamentos_quimioterapicos import MedicamentosQuimioterapicos
from classes.vendas import Vendas
from classes.laboratorios import Laboratorios
from service import relatorios
import re

def interface_cadastrar_cliente():
    cpf = input("Digite o cpf do cliente: ")
    nome = input("Digite o nome do cliente: ")
    data_string = input("Digite a data de nascimento no formato aaaa-mm-dd: ")
    while not validar_data(data_string):
        data_string = input("Data no formato incorreto. Forneça a data de nascimento no formato aaaa-mm-dd: ")
    dn = datetime.strptime(data_string, "%Y-%m-%d").date()
    cliente = Clientes(cpf, nome, dn)
    cliente.cadastrar_cliente()
    print(f"Cliente {nome} cadastrado com sucesso!")

def validar_data(data: str):
    padrao = r"\d{4}-\d{2}-\d{2}"
    if re.match(padrao, data):
        return True

def interface_busca_cliente():
    cpf = input("Digite o cpf do cliente que deseja encontrar: ")
    resultado = Clientes.buscar_cliente(cpf)
    if len(resultado) == 0:
        print(f"Não encontrado cliente para o cpf {cpf}")
    else: 
        print(f"Cliente encontrado: {str(resultado[0])}")

def interface_cadastro_med():
    opcao = "0"
    nome = input("Digite o nome do medicamento: ")
    composto = input("Digite o principal composto do medicamento: ")
    lab = incluir_laboratorio()
    descricao = input("Digite a descrição do medicamento: ")
    valor = float(input("Digite o valor do medicamento: "))
    while opcao not in ["1", "2"]:
        opcao = input("Qual o tipo do medicamento? Digite 1 para Quimioterápico ou 2 para Fitoterápico: ")
        if opcao == "1":
            receita = verifica_controlado()
            quimio = MedicamentosQuimioterapicos(nome, composto, lab, descricao, valor, receita)
            quimio.cadastrar_quimioterapico()
            print(f"Quimioterápico {nome} cadastrado com sucesso!")
            return quimio
        elif opcao =="2":
            fito = MedicamentosFitoterapicos(nome, composto, lab, descricao, valor)
            fito.cadastrar_fitoterapico
            print(f"Fitoterápico {nome} cadastrado com sucesso!")
            return fito
        else:
            print(f"Opção {opcao} inválida!")

def incluir_laboratorio():
    lab_nome = input("Digite o nome do laboratório: ")
    lab_end = input(("Digite o endereço do laboratório: "))
    lab_tel = input(("Digite o telefone do laboratório: "))
    lab_cidade = input(("Digite a cidade onde está localizado o laboratório: "))
    lab_estado = input(("Digite o estado onde está localizado o laboratório: "))
    laboratorio = Laboratorios(lab_nome, lab_end, lab_tel, lab_cidade, lab_estado)
    return laboratorio


def interface_buscar_medicamento():
    sub_menu_busca_med = """
        O que você quer usar para buscar o medicamento?
        1 - Nome
        2 - Fabricante
        3 - Descrição Parcial
        4 - Retornar ao menu anterior\n
        """
    busca = "0"
    while busca not in ['1', '2', '3', '4']:
        busca = input(sub_menu_busca_med)
        if busca == "1":
            nome_med = input("Digite o nome do medicamento: ")
            resultado = Medicamentos.buscar_medicamento(nome = nome_med)
        elif busca == '2':
            lab = input("Digite o nome do laboratório fabricante: ")
            resultado = Medicamentos.buscar_medicamento(fabricante = lab)
        elif busca == '3':
            desc = input("Digite uma descrição parcial: ")
            resultado = Medicamentos.buscar_medicamento(descricao = desc)
        elif busca == '4':
            return " "
        else:
            print(f"Opção {busca} inválida!")

    if len(resultado) == 0:
        print(f"Não encontrado resultado para busca desse medicamento.")
    else: 
        print("\nMedicamentos encontrados: ")
        for med in resultado:
            print(str(med))
    return resultado[0]

def verifica_controlado():
    controlado = " "
    while controlado.lower() not in ['s', 'n']:
        controlado = input("Esse medicamento é controlado? Digite s ou n: ")
        if controlado.lower() == 's':
            receita = True
        elif controlado.lower() == 'n':
            receita = False
        else:
            print(f"Opção {controlado} inválida!")
    return receita
    
def interface_efetuar_venda():
    cpf = input('Insira o cpf do cliente que está efetuando a venda: ')
    cliente = Clientes.buscar_cliente(cpf)
    if len(cliente) == 0:
        print(f'CPF {cpf} não encontrado. Realize o cadastro do cliente antes de efetuar a venda.')
    else:    
        dict_produtos = cadastrar_produtos_venda()
        venda = Vendas(datetime.now(), dict_produtos, cliente[0])
        venda.realizar_venda()
        print("\nVenda realizada com sucesso.")
        print(venda)

def cadastrar_produtos_venda():    
    continua = 's'
    contador = 1
    dict_produtos = {}
    while continua.lower() == 's':
        nome_produto = input(f'Digite o nome do {contador}o medicamento a ser vendido: ')
        medicamento = Medicamentos.buscar_medicamento(nome=nome_produto)
        if len(medicamento) == 0:
            print("Esse medicamento ainda não está cadastrado. Iniciando cadastro: ")
            medicamento = interface_cadastro_med()
        else:
            medicamento = medicamento[0]
        medicamento = confirma_medicamento(medicamento)
        if isinstance(medicamento, MedicamentosQuimioterapicos):
            if medicamento.precisa_receita:
                print(f"Não se esqueça de verificar a receita do medicamento {medicamento.nome}!")
        unidades = int(input("Quantas unidades desse medicamento estão sendo vendidas? "))
        categoria = ""
        if isinstance(medicamento, MedicamentosFitoterapicos):
            categoria = "f"
        elif isinstance(medicamento, MedicamentosQuimioterapicos):
            categoria = "q"
        dict_produtos[medicamento.nome]={"unidades":unidades, "valor_unit": medicamento.valor, "categoria": categoria}
        continua = input("Digite 's' para incluir novo medicamento na venda ou qualquer outra tecla para encerrar a venda: ")
        contador +=1
    return dict_produtos

def confirma_medicamento(medicamento):
    confirma = " "
    med = medicamento
    while confirma != 's':
        confirma = input(f"Confirma inclusão do medicamento {med.nome} na compra? Digite 's' para incluir ou 'n' para realizar nova busca: ")
        if confirma == 'n':
            med = interface_buscar_medicamento()
    return med
        

def interface_emissao_relatorios():
    sub_menu_relatorios = """
        Qual o relatório que você deseja emitir?
        1 - Lista de clientes
        2 - Lista de medicamentos
        3 - Lista de medicamentos por tipo
        4 - Retornar ao menu anterior\n
        """
    opcao = 0
    while opcao not in ["1", "2", "3", "4"]:
        opcao = input(sub_menu_relatorios)
        if opcao == '1':
            relatorios.criar_relatorio_cliente()
        elif opcao == '2':
            relatorios.criar_relatorio_medicamentos()
        elif opcao == '3':
            tipo_med = escolher_tipo_medicamento()
            relatorios.criar_relatorio_med_especifico(tipo_med)
        elif opcao == '4':
            return " "
        else:
            print(f"Opção {opcao} inválida!")
            

def escolher_tipo_medicamento():
    tipo = " "
    while tipo.lower() not in ['f', 'q']:
        tipo = input("Digite 'f' para listar fitoterápicos ou 'q' para quimioterápicos: ")
    return tipo
