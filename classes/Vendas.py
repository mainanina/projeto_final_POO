from datetime import datetime
from classes.clientes import Clientes

class Vendas:

    vendas_dia = []

    def __init__(self, dt_hr_venda: datetime, prod_vend: dict, cliente: Clientes):
        self._hora_venda = dt_hr_venda
        self._produtos = prod_vend
        self._cliente = cliente
        self._valor = self.calcular_valor_venda(prod_vend)

    def __str__(self):
        return f'''
        Cliente: {self.nome} - CPF: {self.cpf}
        {self.mostrar_produtos()}
        Valor total: R$ {round(self.valor, 2)}
        '''

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

    def realizar_venda(self):
        self.vendas_dia.append(self)

    def calcular_valor_venda(self):
        total_venda = 0
        for qtdd, item in self.prod_vend:
            parcial = qtdd * item.valor
            total_venda +=parcial
        valor_final = self.aplicar_desconto(self.cliente, total_venda)
        return valor_final
    
    def aplicar_desconto(self, total_venda: float):
        if self.cliente.calcular_idade()>65:
            valor_final = total_venda * 0.8
        elif total_venda>150:
            valor_final = total_venda * 0.9
        return valor_final
    
    def mostrar_produtos(self):
        for chave, valor in self.produtos:
            print(f'{chave.nome}: {valor} unidades')
