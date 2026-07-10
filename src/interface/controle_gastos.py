from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Prompt
from rich import box
from datetime import datetime
from dados.dados import carregar_json
from financeiro.calculos import obter_resumo

console = Console()

CATEGORIAS = [
    {"nome": "Alimentação", "gasto": 980.00, "limite": 1200.00, "cor": "green"},
    {"nome": "Transporte",  "gasto": 540.00, "limite": 600.00,  "cor": "yellow"},
    {"nome": "Moradia",     "gasto": 1500.00, "limite": 1500.00, "cor": "red"},
    {"nome": "Lazer",       "gasto": 310.25, "limite": 500.00,  "cor": "cyan"},
    {"nome": "Saúde",       "gasto": 219.00, "limite": 400.00,  "cor": "blue"},
]

MENU_OPCOES = [
    ("1", "📊 Dashboard"),
    ("2", "💸 Transações"),
    ("3", "🗂️  Categorias"),
    ("4", "📈 Relatórios"),
    ("5", "⚙️  Vazio"),
    ("0", "🚪 Sair"),
]

def montar_cabecalho() -> Panel:
    titulo = Text("💰  CONTROLE DE GASTOS", style="bold white on dark_green", justify="center")
    subtitulo = Text(f"Bem-vindo(a), Usuário  •  {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                      style="dim", justify="center")
    conteudo = Text.assemble(titulo, "\n", subtitulo)
    return Panel(Align.center(conteudo), box=box.DOUBLE, style="on grey11", padding=(0, 2))


def montar_menu_lateral(opcao_ativa: str) -> Panel:
    texto = Text()
    for chave, nome in MENU_OPCOES:
        if chave == opcao_ativa:
            texto.append(f" ➤ [{chave}] {nome}\n", style="bold black on green")
        else:
            texto.append(f"   [{chave}] {nome}\n", style="white")
    return Panel(texto, title="MENU", border_style="green", box=box.ROUNDED)


def montar_cards_resumo() -> Table:
    tabela = Table.grid(expand=True)
    tabela.add_column(ratio=1)
    tabela.add_column(ratio=1)
    tabela.add_column(ratio=1)

    resumo = obter_resumo()

    card_saldo = Panel(
        Align.center(Text(f"R$ {resumo['saldo']:.2f}", style="bold green")),
        title="💼 Saldo Atual", border_style="green", box=box.ROUNDED,
    )
    card_receitas = Panel(
        Align.center(Text(f"R$ {resumo['receitas']:.2f}", style="bold cyan")),
        title="⬆️  Receitas", border_style="cyan", box=box.ROUNDED,
    )
    card_despesas = Panel(
        Align.center(Text(f"R$ {resumo['despesas']:.2f}", style="bold red")),
        title="⬇️  Despesas", border_style="red", box=box.ROUNDED,
    )
    tabela.add_row(card_saldo, card_receitas, card_despesas)
    return tabela


def montar_tabela_transacoes() -> Panel:
    tabela = Table(box=box.SIMPLE_HEAVY, expand=True, show_lines=False)

    tabela.add_column("Data", style="dim", width=10)
    tabela.add_column("Descrição", style="white")
    tabela.add_column("Categoria", style="magenta")
    tabela.add_column("Tipo", justify="center")
    tabela.add_column("Valor", justify="right")

    transacoes = carregar_json()

    for t in transacoes:
        cor_valor = "green" if t["tipo"] == "receita" else "red"
        sinal = "+" if t["tipo"] == "receita" else "-"

        tabela.add_row(
            t["data"],
            t["descricao"],
            t["categoria"],
            f"[{cor_valor}]{t['tipo']}[/]",
            f"[{cor_valor}]{sinal} R$ {t['valor']:.2f}[/]",
        )

    return Panel(
        tabela,
        title="🧾 Últimas Transações",
        border_style="blue",
        box=box.ROUNDED
    )

def montar_categorias() -> Panel:
    progress = Progress(
        TextColumn("[bold]{task.fields[nome]:<14}"),
        BarColumn(bar_width=30),
        TextColumn("R$ {task.fields[gasto]:.2f} / R$ {task.fields[limite]:.2f}"),
        expand=True,
    )
    for c in CATEGORIAS:
        progress.add_task("", total=c["limite"], completed=c["gasto"],
                           nome=c["nome"], gasto=c["gasto"], limite=c["limite"])
    return Panel(progress, title="🗂️  Gastos por Categoria", border_style="yellow", box=box.ROUNDED)


def montar_meta() -> Panel:
    resumo = obter_resumo()

    pct = resumo["economizado"] / resumo["meta_economia"] * 100

    barra = Progress(
        TextColumn("Meta de Economia"),
        BarColumn(bar_width=40, complete_style="bright_green"),
        TextColumn(f"{pct:.0f}%"),
    )

    barra.add_task(
        "",
        total=resumo["meta_economia"],
        completed=resumo["economizado"]
    )

    return Panel(
        barra,
        border_style="bright_green",
        box=box.ROUNDED
    )


def montar_rodape(mensagem: str = "") -> Panel:
    dica = "Digite o número da opção desejada e pressione Enter."
    texto = Text(mensagem or dica, style="italic dim", justify="center")
    return Panel(texto, box=box.MINIMAL, style="on grey15")



# TELAS


def tela_dashboard():
    console.print(montar_cards_resumo())
    console.print()
    console.print(montar_meta())
    console.print()
    console.print(montar_tabela_transacoes())


def tela_transacoes():
    console.print(montar_tabela_transacoes())
    console.print()
    console.print(Panel(
        "[dim]➕ Adicionar nova transação   ✏️ Editar   🗑️ Excluir[/dim]\n"
        "[bold yellow](funcionalidade ainda não implementada - somente interface)[/bold yellow]",
        title="Ações", border_style="grey50", box=box.ROUNDED,
    ))


def tela_categorias():
    console.print(montar_categorias())
    console.print()
    console.print(Panel(
        "[dim]➕ Nova categoria   ✏️ Editar limite[/dim]\n"
        "[bold yellow](funcionalidade ainda não implementada - somente interface)[/bold yellow]",
        title="Ações", border_style="grey50", box=box.ROUNDED,
    ))


def tela_relatorios():
    tabela = Table(box=box.SIMPLE, expand=True)
    tabela.add_column("Mês")
    tabela.add_column("Receitas", justify="right")
    tabela.add_column("Despesas", justify="right")
    tabela.add_column("Saldo", justify="right")
    dados_mock = [
        ("Maio/2026", 6500.00, 4100.00),
        ("Junho/2026", 6800.00, 3890.00),
        ("Julho/2026", 6800.00, 3549.25),
    ]
    for mes, receita, despesa in dados_mock:
        saldo = receita - despesa
        cor = "green" if saldo >= 0 else "red"
        tabela.add_row(mes, f"R$ {receita:.2f}", f"R$ {despesa:.2f}", f"[{cor}]R$ {saldo:.2f}[/]")
    console.print(Panel(tabela, title="📈 Relatório Mensal (dados fictícios)", border_style="cyan", box=box.ROUNDED))


TELAS = {
    "1": ("Dashboard", tela_dashboard),
    "2": ("Transações", tela_transacoes),
    "3": ("Categorias", tela_categorias),
    "4": ("Relatórios", tela_relatorios),
}

# LOOP PRINCIPAL

def renderizar(opcao_ativa: str, mensagem: str = ""):
    console.clear()
    console.print(montar_cabecalho())
    console.print()

    layout = Table.grid(expand=True)
    layout.add_column(ratio=1)
    layout.add_column(ratio=4)

    lado_esquerdo = montar_menu_lateral(opcao_ativa)

    console.print(layout)
    console.print(Align.left(lado_esquerdo))
    console.print()

    nome_tela, funcao_tela = TELAS.get(opcao_ativa, ("Dashboard", tela_dashboard))
    console.rule(f"[bold]{nome_tela}[/bold]", style="green")
    funcao_tela()
    console.print()
    console.print(montar_rodape(mensagem))


def main():
    opcao_ativa = "1"
    mensagem = ""
    while True:
        renderizar(opcao_ativa, mensagem)
        escolha = Prompt.ask(
            "\n[bold cyan]Escolha uma opção[/bold cyan]",
            choices=[c for c, _ in MENU_OPCOES],
            show_choices=False,
        )
        if escolha == "0":
            console.clear()
            console.print(Panel(
                Align.center(Text("Até logo! 👋", style="bold green")),
                box=box.DOUBLE, border_style="green",
            ))
            break
        elif escolha in TELAS:
            opcao_ativa = escolha
            mensagem = ""
        else:
            mensagem = "[red]Opção inválida.[/red]"


if __name__ == "__main__":
    main()
