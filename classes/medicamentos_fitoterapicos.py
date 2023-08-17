from classes import medicamentos

class MedicamentosFitoterapicos(medicamentos.Medicamentos):
    
    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str, valor: float):
        super().__init__(nome, pp_composto, lab, descricao, valor)

    def cadastrar_fitoterapico(self, nome: str, pp_composto: str, laboratorio: str, descricao: str, valor: float):
        medicamento = MedicamentosFitoterapicos(nome, pp_composto, laboratorio, descricao, valor)
        super().cadastro_medicamentos.append(medicamento)
        print(f"Fitoterápico {nome} cadastrado com sucesso!")