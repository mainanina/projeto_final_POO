class Laboratorios:
    '''
        Classe para modelar laboratórios fabricantes de medicamentos.
        nome: nome do laboratório
        endereço: endereço do laboratório
    '''


    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str): 
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cidade = cidade
        self._estado = estado


    def __str__(self):
        return f"""
        Nome: {self.nome}
        Telefone: {self.telefone}
        Endereço: {self.endereco} - {self.cidade}, {self.estado}
        """


    @property
    def nome(self):
        return self._nome
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def cidade(self):
        return self._cidade
    
    @property
    def estado(self):
        return self._estado
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @estado.setter
    def estado(self, estado):
        self._estado = estado
