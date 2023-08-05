from classes import Medicamentos

class MedicamentosQuimioterapicos(Medicamentos):

    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str, receita: bool):
        super().__init__(nome, pp_composto, lab, descricao)
        self._precisa_receita = receita

    @property
    def precisa_receita(self):
        return self._precisa_receita
    
    @precisa_receita.setter
    def precisa_receita(self, precisa_receita):
        self._precisa_receita = precisa_receita