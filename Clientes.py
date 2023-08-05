from datetime import date

class Clientes:

    def __init__(self, cpf: str, nome: str, dn: date): 
        self._cpf = cpf
        self._nome = nome
        self._dn = dn

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def dn(self):
        return self._dn
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @dn.setter
    def dn(self, dn):
        self._dn = dn