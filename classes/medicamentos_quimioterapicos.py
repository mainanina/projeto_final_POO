from classes import medicamentos

class MedicamentosQuimioterapicos(medicamentos.Medicamentos):

    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str, valor: float, receita: bool):
        super().__init__(nome, pp_composto, lab, descricao, valor)
        self._precisa_receita = receita
    
    def __str__(self):
        return f"""
            Nome: {self.nome}
            Principal Composto: {self.pp_composto}
            Laboratório: {self.laboratorio}
            Descrição: {self.descricao}
            Valor: {self.valor}
            Precisa de receita? {self.precisa_receita}
            """

    @property
    def precisa_receita(self):
        return self._precisa_receita
    
    @precisa_receita.setter
    def precisa_receita(self, precisa_receita):
        self._precisa_receita = precisa_receita

    def cadastrar_quimioterapico(self):
        super().cadastro_medicamentos.append(self)
        