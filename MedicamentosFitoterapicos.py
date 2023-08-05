from projeto_final_POO import Medicamentos

class MedicamentosFitoterapicos(Medicamentos):
    
    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str):
        super().__init__(nome, pp_composto, lab, descricao)