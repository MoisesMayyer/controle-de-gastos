from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich import box
from rich.console import Console


console = Console()

categorias = []

def montar_categorias() -> Panel:
    progress = Progress(
        TextColumn("[bold]{task.fields[nome]:<14}"),
        BarColumn(bar_width=30),
        TextColumn("R$ {task.fields[gasto]:.2f} / R$ {task.fields[limite]:.2f}"),
        expand=True,
    )
    if categorias:
        for c in categorias:
            progress.add_task("", total=c["limite"], completed=c["gasto"],
                               nome=c["nome"], gasto=c["gasto"], limite=c["limite"])
        return Panel(progress, title="🗂️  Gastos por Categoria", border_style="yellow", box=box.ROUNDED)
    else:
        return Panel(
            "Nenhuma categoria cadastrada.",
            title="🗂️ Gastos por Categoria",
            border_style="yellow",
            box=box.ROUNDED,
        )