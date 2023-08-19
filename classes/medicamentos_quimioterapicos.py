from classes import medicamentos
from classes.laboratorios import Laboratorios

class MedicamentosQuimioterapicos(medicamentos.Medicamentos):
    '''
        Classe para que especializa a classe Medicamentos em Quimioterápicos.
        Adiciona o parâmetro precisa_receita -> quando True, significa que o medicamento é controlado e
            portantoé obrigatório apresentar a receita na hora da compra.
    '''
     

    def __init__(self, nome: str, pp_composto: str, lab: Laboratorios, descricao: str, valor: float, receita: bool):
        super().__init__(nome, pp_composto, lab, descricao, valor)
        self._precisa_receita = receita
    

    def __str__(self):
        return f"""
            Nome: {self.nome}
            Principal Composto: {self.pp_composto}
            Laboratório: {self.laboratorio.nome}
            Descrição: {self.descricao}
            Valor: {self.valor}
            Classe: Quimioterápico
            Precisa de receita? {self.precisa_receita}
            """


    @property
    def precisa_receita(self):
        return self._precisa_receita
    
    @precisa_receita.setter
    def precisa_receita(self, precisa_receita):
        self._precisa_receita = precisa_receita


    def cadastrar_quimioterapico(self):
        '''
        Adiciona o medicamento quimioterápico ao cadastro geral de medicamentos
        '''
        super().cadastro_medicamentos.append(self)
        