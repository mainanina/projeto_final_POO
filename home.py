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
        7 - Emitir Relatório de vendas do dia e sair\n
        """
    #vendas do dia com 7? ou 6?

    sub_menu_busca_med = """
        O que você quer usar para buscar o medicamento?
        1 - Nome
        2 - Fabricante
        3 - Descrição Parcial
        """
    
    # NO 3 é ou?? Ou tem que escolher?
    sub_menu_relatorios = """
        Qual o relatório que você deseja omitir?
        1 - Lista de clientes
        2 - Lista de medicamentos
        3 - Lista de quimioterápicos e fitoterápicos
        4 - Atendimentos do dia
        """
    
    opcao = input(menu_str)
    if opcao == "1":
        pass
    elif opcao == "2":
       pass
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


if __name__ == "__main__":
    print("\nBoas-vindas ao nosso sistema!")
    menu()