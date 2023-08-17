from datetime import date
import datetime

class Clientes:

    cadastro_clientes = []

    def __init__(self, cpf: str, nome: str, dn: date): 
        self._cpf = cpf
        self._nome = nome
        self._dn = dn

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Principal Composto: {self.pp_composto}
        Laboratório: {self.laboratorio}
        Descrição: {self.descricao}
        """

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def dn(self):
        return self._dn

    @nome.setter
    def nome(self, nome):
        self._nome = nome


    def cadastrar_cliente(self, cpf: str, nome: str, dn: date):
        cliente =  Clientes(cpf, nome, dn)
        self.cadastro_cliente.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")


    def buscar_cliente(self, cpf: str):
        resultado = [cliente for cliente in self.cadastro_clientes if cliente.cpf == cpf]
        if len(resultado) == 0:
            print(f"Não encontrado cliente para o cpf {cpf}")
        else: 
            print(f"Cliente encontrado: {str(resultado[0])}")

    def calcular_idade(self):
        hoje = datetime.today().date()
        idade = hoje.year - self.dn.year - ((hoje.month, hoje.day) < (self.dn.month, self.dn.day))
        return idade
