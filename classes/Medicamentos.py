class Medicamentos:

    def __init__(self, nome: str, pp_composto: str, lab: str, descricao: str):
        self._nome = nome
        self._pp_composto = pp_composto
        self._laboratorio = lab
        self._descricao = descricao

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