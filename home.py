from helper import chamadas_menu, relatorios


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


if __name__ == "__main__":
    print("\nBoas-vindas ao nosso sistema!")
    menu()