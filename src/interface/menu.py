from rich.console import Console
from rich.prompt import Prompt

from interface.componentes import (
    montar_cabecalho,
    montar_menu_lateral,
    montar_rodape
)

from interface.dashboard import tela_dashboard
from interface.menu_transacoes import tela_transacoes


console = Console()


menu_opcoes = [
    ("1", "📊 Dashboard"),
    ("2", "💸 Transações"),
    ("0", "🚪 Sair"),
]


TELAS = {
    "1": tela_dashboard,
    "2": tela_transacoes,
}


def iniciar_menu():

    opcao_ativa = "1"

    while True:

        console.clear()

        console.print(
            montar_cabecalho()
        )

        console.print(
            montar_menu_lateral(
                opcao_ativa,
                menu_opcoes
            )
        )

        console.print()

        tela = TELAS.get(opcao_ativa)

        if tela:
            tela()


        escolha = Prompt.ask(
            "Escolha uma opção",
            choices=["1", "2", "0"]
        )


        if escolha == "0":
            console.print(
                montar_rodape("Até logo!")
            )
            break


        opcao_ativa = escolha