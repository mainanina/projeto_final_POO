from datetime import date

class Clientes:

    cadastro_clientes = []

    def __init__(self, cpf: str, nome: str, dn: date): 
        self._cpf = cpf
        self._nome = nome
        self._dn = dn

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def dn(self):
        return self._dn

    @nome.setter
    def nome(self, nome):
        self._nome = nome


    def cadastrar_cliente(self, cpf: str, nome: str, dn: date):
        cliente =  Clientes(cpf, nome, dn)
        self.cadastro_cliente.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return cliente


    def buscar_cliente(self, cpf: str):
        resultado = [cliente for cliente in self.cadastro_clientes if cliente.cpf == "cpf"]
        if len(resultado) == 0:
            print("CPF não encontrado")
        else: 
            print(f"Cliente encontrado: {str(resultado[0])}")
            return resultado[0]
