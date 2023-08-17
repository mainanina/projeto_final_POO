from datetime import datetime
from classes.clientes import Clientes
from classes.medicamentos import Medicamentos
from classes.medicamentos_fitoterapicos import MedicamentosFitoterapicos
from classes.medicamentos_quimioterapicos import MedicamentosQuimioterapicos
from classes.vendas import Vendas
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
    