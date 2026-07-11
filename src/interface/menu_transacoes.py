from rich.console import Console
from rich.panel import Panel
from rich import box

from financeiro.transacoes import (
    adicionar_transacao,
    editar_transacao,
    remover_transacao
)


console = Console()


def tela_transacoes():

    console.print(
        Panel(
            "[1] Adicionar\n"
            "[2] Editar\n"
            "[3] Excluir\n"
            "[4] Voltar",
            title="Transações",
            border_style="blue",
            box=box.ROUNDED
        )
    )

    submenu_transacoes()



def submenu_transacoes():

    while True:

        try:
            opcao = int(input("Digite sua opção: "))

        except ValueError:
            print("Opção inválida!")
            continue


        if opcao == 1:
            adicionar_transacao()

        elif opcao == 2:
            editar_transacao()

        elif opcao == 3:
            remover_transacao()

        elif opcao == 4:
            break

        else:
            print("Opção inexistente!")