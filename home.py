from helper import relatorios, chamadas_menu


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

    sub_menu_busca_med = """
        O que você quer usar para buscar o medicamento?
        1 - Nome
        2 - Fabricante
        3 - Descrição Parcial
        """
    
    sub_menu_relatorios = """
        Qual o relatório que você deseja emitir?
        1 - Lista de clientes
        2 - Lista de medicamentos
        3 - Lista de quimioterápicos e fitoterápicos
        4 - Atendimentos do dia
        """
    
    opcao = "0"
    while opcao != "7":
        opcao = input(menu_str)
        if opcao == "1":
            chamadas_menu.interface_cadastrar_cliente()
        elif opcao == "2":
           chamadas_menu.interface_busca_cliente()
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            pass
        elif opcao == "7":
            pass
        else:
            print(f"Essa opção ({opcao}) não é válida!")


if __name__ == "__main__":
    print("\nBoas-vindas ao nosso sistema!")
    menu()