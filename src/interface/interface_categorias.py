from rich.panel import Panel
from rich.console import Console
from rich import box
from interface.categorias_menu import montar_categorias
from financeiro.categorias import nova_categoria, remover_categoria, editar_categoria


console = Console()


def tela_categorias():
    console.print(montar_categorias())
    console.print()
    console.print(Panel(
        "[dim][1] Nova categoria   [2] Editar limite   [3] Remover categoria   [4] Sair[/dim]\n"
        "[bold yellow](funcionalidade ainda não implementada - somente interface)[/bold yellow]",
        title="Ações", border_style="grey50", box=box.ROUNDED,
    ))
    submenu_categorias()


def submenu_categorias():
    while True:
        try:
            opcao = int(input("Digite sua opção: "))

        except ValueError:
            print("Opção inválida!")
            continue

        if opcao == 1:
            nova_categoria()
            break
        elif opcao == 2:
            editar_categoria()
        elif opcao == 3:
            remover_categoria()
        elif opcao == 4:
            break
        else:
            print("opcão invalida!")