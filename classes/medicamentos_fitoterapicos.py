from classes import medicamentos
from classes.laboratorios import Laboratorios

class MedicamentosFitoterapicos(medicamentos.Medicamentos):
    '''
        Classe para que especializa a classe Medicamentos em Fitoterápicos
    '''
    

    def __init__(self, nome: str, pp_composto: str, lab: Laboratorios, descricao: str, valor: float):
        super().__init__(nome, pp_composto, lab, descricao, valor)


    def __str__(self):
        return f"""
            Nome: {self.nome}
            Principal Composto: {self.pp_composto}
            Laboratório: {self.laboratorio.nome}
            Descrição: {self.descricao}
            Valor: {self.valor}
            Classe: Fitoterápico
            """


    def cadastrar_fitoterapico(self):
        '''
        Adiciona o medicamento fitoterápico ao cadastro geral de medicamentos
        '''
        super().cadastro_medicamentos.append(self)