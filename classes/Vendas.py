from datetime import datetime
from classes import Clientes

class Vendas:

    def __init__(self, dt_hr_venda: datetime, prod_vend: list, cliente: Clientes, valor: float):
        self._hora_venda = dt_hr_venda
        self._produtos = prod_vend
        self._cliente = cliente
        self._valor = valor

    @property
    def hora_venda(self):
        return self._hora_venda
    
    @property
    def produtos(self):
        return self._produtos
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def valor(self):
        return self._valor
    
    @hora_venda.setter
    def hora_venda(self, hora_venda):
        self._hora_venda = hora_venda

    @produtos.setter
    def produtos(self, produtos):
        self._produtos = produtos

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @valor.setter
    def valor(self, valor):
        self._valor = valor