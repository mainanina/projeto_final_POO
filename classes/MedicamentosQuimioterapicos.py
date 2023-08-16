from classes import Medicamentos

class MedicamentosQuimioterapicos(Medicamentos):

    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str, valor: float, receita: bool):
        super().__init__(nome, pp_composto, lab, descricao, valor)
        self._precisa_receita = receita
        if receita:
            print(f"Não se esqueça de verificar a receita do medicamento {nome}")

    @property
    def precisa_receita(self):
        return self._precisa_receita
    
    @precisa_receita.setter
    def precisa_receita(self, precisa_receita):
        self._precisa_receita = precisa_receita

    def cadastrar_quimioterapico(self, nome: str, pp_composto: str, laboratorio: str, descricao: str, valor: float, receita: bool):
        medicamento = MedicamentosQuimioterapicos(nome, pp_composto, laboratorio, descricao, valor, receita)
        super().cadastro_medicamentos.append(medicamento)
        print(f"Quimioterápico {nome} cadastrado com sucesso!")