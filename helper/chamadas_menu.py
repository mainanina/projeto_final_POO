from datetime import datetime
from classes.clientes import Clientes
from classes.medicamentos import Medicamentos
from classes.medicamentos_fitoterapicos import MedicamentosFitoterapicos
from classes.medicamentos_quimioterapicos import MedicamentosQuimioterapicos
from classes.vendas import Vendas

def interface_cadastrar_cliente():
    cpf = input("Digite o cpf do cliente: ")
    nome = input("Digite o nome do cliente: ")
    ano = input("Digite o ano de nascimento com 4 digitos: ")
    mes = input("Digite o mês de nascimento com 2 digitos: ")
    dia = input("Digite o dia do nascimento: ")
    data_string = f"{ano}-{mes}-{dia}"
    dn = datetime.strptime(data_string, "%Y-%m-%d").date()
    cliente = Clientes(cpf, nome, dn)
    cliente.cadastrar_cliente()
    print(f"Cliente {nome} cadastrado com sucesso!")

def interface_busca_cliente():
    cpf = input("Digite o cpf do cliente que deseja encontrar: ")
    resultado = Clientes.buscar_cliente(cpf)
    if len(resultado) == 0:
        print(f"Não encontrado cliente para o cpf {cpf}")
    else: 
        print(f"Cliente encontrado: {str(resultado[0])}")
    