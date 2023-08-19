from classes.laboratorios import Laboratorios

class Medicamentos:

    cadastro_medicamentos = []

    def __init__(self, nome: str, pp_composto: str, lab: Laboratorios, descricao: str, valor: float):
        self._nome = nome
        self._pp_composto = pp_composto
        self._laboratorio = lab
        self._descricao = descricao
        self._valor = valor

    def __str__(self):
        return f"""
            Nome: {self.nome}
            Principal Composto: {self.pp_composto}
            Laboratório: {self.laboratorio.nome}
            Descrição: {self.descricao}
            Valor: {self.valor}
            """

    @property
    def nome(self):
        return self._nome
    
    @property
    def pp_composto(self):
        return self._pp_composto
    
    @property
    def laboratorio(self):
        return self._laboratorio
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def valor(self):
        return self._valor
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @pp_composto.setter
    def pp_composto(self, pp_composto):
        self._pp_composto = pp_composto

    @laboratorio.setter
    def laboratorio(self, lab):
        self._laboratorio = lab

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @staticmethod
    def buscar_medicamento(nome = None, fabricante = None, descricao = None):
        if nome is not None:
            resultado = [med for med in Medicamentos.cadastro_medicamentos if  nome.lower() in med.nome.lower()]
        elif fabricante is not None:
            resultado = [med for med in Medicamentos.cadastro_medicamentos if fabricante.lower() in med.laboratorio.nome.lower()]
        elif descricao is not None:
            resultado = [med for med in Medicamentos.cadastro_medicamentos if descricao.lower() in med.descricao.lower()]
        return resultado
        
