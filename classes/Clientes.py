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
        CPF: {self.cpf}
        Idade: {self.calcular_idade()}
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


    def cadastrar_cliente(self):
        self.cadastro_clientes.append(self)

    @staticmethod
    def buscar_cliente(cpf: str):
        return [cliente for cliente in Clientes.cadastro_clientes if cliente.cpf == cpf]

    def calcular_idade(self):
        hoje = date.today()
        idade = hoje.year - self.dn.year - ((hoje.month, hoje.day) < (self.dn.month, self.dn.day))
        return idade
