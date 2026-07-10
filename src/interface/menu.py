from financeiro.transacoes import (
    adicionar_transacao,
    listar_transacoes,
    remover_transacao,
    editar_transacao,
    total_despesas
)


def menu():
    print("=" * 5, "controle de gastos", "=" * 5)
    print(
        "1 - Adicionar gasto\n"
        "2 - Listar gastos\n"
        "3 - Total gasto\n"
        "4 - Sair"
    )


def sub_menu():
    while True:
        try:
            opcao_lista = int(
                input(
                    "Remover [1] / Editar [2] / Voltar [3]: "
                )
            )
        except ValueError:
            print("Digite apenas números.")
            continue

        if opcao_lista == 1:
            remover_transacao()

        elif opcao_lista == 2:
            editar_transacao()

        elif opcao_lista == 3:
            break

        else:
            print("Opção inválida!")


# menu temporário
def iniciar():
    while True:

        menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("opção invalida")
            print("Digite apenas números")
            continue

        if opcao == 1:
            adicionar_transacao()

        elif opcao == 2:
            listar_transacoes()
            sub_menu()

        elif opcao == 3:
            total_despesas()
        else:
            break
