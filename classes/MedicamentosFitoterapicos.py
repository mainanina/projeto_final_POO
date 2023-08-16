from classes import Medicamentos

class MedicamentosFitoterapicos(Medicamentos):
    
    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str):
        super().__init__(nome, pp_composto, lab, descricao)

    def cadastrar_fitorerapico(self, nome: str, pp_composto: str, laboratorio: str, descricao: str, valor: float):
        medicamento = MedicamentosFitoterapicos(nome, pp_composto, laboratorio, descricao, valor)
        super().cadastro_medicamentos.append(medicamento)
        print(f"Fitoterápico {nome} cadastrado com sucesso!")