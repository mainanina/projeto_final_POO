from classes import medicamentos

class MedicamentosFitoterapicos(medicamentos.Medicamentos):
    
    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str, valor: float):
        super().__init__(nome, pp_composto, lab, descricao, valor)

    def __str__(self):
        return f"""
            Nome: {self.nome}
            Principal Composto: {self.pp_composto}
            Laboratório: {self.laboratorio}
            Descrição: {self.descricao}
            Valor: {self.valor}
            Classe: Fitoterápico
            """

    def cadastrar_fitoterapico(self):
        super().cadastro_medicamentos.append(self)