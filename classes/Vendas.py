from datetime import datetime
from classes.clientes import Clientes

class Vendas:
    '''
    Classe para modelar as operações de venda.
    hora_venda: data e hora da venda, registrados automaticamente de acordo com o horário do sistema
    produtos: dicionario contendo nome do produto, quantidade de unidades vendidas, preco unitario e 
        categoria (quimioterápico ou fitoterápico)
    cliente: cliente que realizou a venda
    vendas_dia: lista com registro de todas as vendas realizadas entre a inicialização do sistema e o 
        seu fechamento.
    '''
    vendas_dia = []


    def __init__(self, dt_hr_venda: datetime, prod_vend: dict, cliente: Clientes):
        self._hora_venda = dt_hr_venda
        self._produtos = prod_vend
        self._cliente = cliente
        self._valor , self._desconto= self.calcular_valor_venda()


    def __str__(self):
        return f'''
        Data e Horário: {self.hora_venda}
        Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf}
        {self.mostrar_produtos()}
        Valor total: R$ {round(self.valor, 2)} {self.mostrar_desconto()}
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
    
    @property
    def desconto(self):
        return self._desconto
    
    @hora_venda.setter
    def hora_venda(self, hora_venda):
        self._hora_venda = hora_venda

    @produtos.setter
    def produtos(self, produtos):
        self._produtos = produtos

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente


    def realizar_venda(self):
        self.vendas_dia.append(self)


    def calcular_valor_venda(self):
        '''
        Faz o cálculo do valor total da venda baseado nos produtos vendidos, suas quantidades e seu
        valor unitário, já aplicando os devidos descontos.
        '''
        total_venda = 0
        for item, valor in self.produtos.items():
            parcial = valor['unidades'] * valor["valor_unit"]
            total_venda +=parcial
        desconto = self.calcular_desconto(total_venda)
        if desconto !=0:
            total_venda = total_venda*desconto
        return total_venda, desconto
    

    def calcular_desconto(self, total_venda: float):
        '''
        Calcula o desconto de acordo com a regra de negócio: 
        20% para pessoas com mais de 65 anos e 10% em compras acima de R$150.
        Os descontos não se acumulam, prevalecendo o maior deles.
        '''
        desconto = 0
        if self.cliente.calcular_idade()>65:
            desconto = 0.8
        elif total_venda>150:
            desconto = 0.9
        return desconto
    

    def mostrar_produtos(self):
        '''
        Função que formata para o terminal a apresentação da lista de produtos
        '''
        lista = []
        for item, valor in self.produtos.items():
            lista.append(f"{item}: {valor['unidades']} unidade(s)")
        return lista
    

    def mostrar_desconto(self):
        '''
        Função que apresenta o desconto recebido no terminal para o cliente quando existe desconto.
        ''' 
        if self.desconto == 0:
            return ""
        else:
            return f" -> houve desconto de {100-(round(self.desconto*100))}% no valor total da venda!"