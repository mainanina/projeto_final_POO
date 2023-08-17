from classes import medicamentos

class MedicamentosFitoterapicos(medicamentos.Medicamentos):
    
    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str, valor: float):
        super().__init__(nome, pp_composto, lab, descricao, valor)

    def cadastrar_fitoterapico(self):
        super().cadastro_medicamentos.append(self)