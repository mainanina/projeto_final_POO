from helper import chamadas_menu, relatorios
from classes.clientes import Clientes
from classes.medicamentos_fitoterapicos import MedicamentosFitoterapicos
from classes.medicamentos_quimioterapicos import MedicamentosQuimioterapicos
from datetime import datetime


def menu():
    '''
        Função principal que inicializa o menu e faz a chamada das funções
        do programa de acordo com a opção escolhida
    '''
    menu_str = """
        Digite a opção desejada:
        1 - Cadastrar cliente
        2 - Buscar cliente pelo cfp
        3 - Cadastrar medicamento
        4 - Buscar medicamento
        5 - Efetuar Venda
        6 - Emitir Relatórios
        7 - Sair\n
        """
    
    opcao = "0"
    while opcao != "7":
        opcao = input(menu_str)
        if opcao == "1":
            chamadas_menu.interface_cadastrar_cliente()
        elif opcao == "2":
           chamadas_menu.interface_busca_cliente()
        elif opcao == "3":
            chamadas_menu.interface_cadastro_med()
        elif opcao == "4":
            chamadas_menu.interface_buscar_medicamento()
        elif opcao == "5":
            chamadas_menu.interface_efetuar_venda()
        elif opcao == "6":
            chamadas_menu.interface_emissao_relatorios()
        elif opcao == "7":
            print("Obrigada por utilizar o nosso sistema!\n")
            relatorios.criar_relatorio_dia()
        else:
            print(f"Essa opção ({opcao}) não é válida!")

def inicializar_cadastro():
    cliente1 = Clientes("98765432987", "José da Silva", datetime.strptime("1980-10-25", "%Y-%m-%d").date())
    Clientes.cadastrar_cliente(cliente1)
    cliente2 = Clientes("87539036471", "Camila Ribeiro", datetime.strptime("1990-04-02", "%Y-%m-%d").date())
    Clientes.cadastrar_cliente(cliente2)
    cliente3 = Clientes("46990040985", "Melissa Alves", datetime.strptime("2000-07-11", "%Y-%m-%d").date())
    Clientes.cadastrar_cliente(cliente3)
    fito1 = MedicamentosFitoterapicos("Maracujina", "Maracujae Paxis", "Ache", "Calmante natural à base de plantas", 24.98)
    MedicamentosFitoterapicos.cadastrar_fitoterapico(fito1)
    fito2 = MedicamentosFitoterapicos("Dormex", "Melissa officinalis", "Abex", "Tratamento a base de plantas de combate à insônia e à ansiedade", 19.35)
    MedicamentosFitoterapicos.cadastrar_fitoterapico(fito2)
    quimio1 = MedicamentosQuimioterapicos("Onconex", "Minezantrol", "SNFC", "Quimioterápico para tratamento do câncer de intestino tipo 3")
    MedicamentosQuimioterapicos.cadastrar_quimioterapico(quimio1)
    quimio2 = MedicamentosQuimioterapicos("Denolet", "Finoxy", "Finnit", "Quimioterápico indicado para o tratamento de cancer de próstata")
    MedicamentosQuimioterapicos.cadastrar_quimioterapico(quimio2)


if __name__ == "__main__":
    print("\nBoas-vindas ao nosso sistema!")
    inicializar_cadastro()
    menu()