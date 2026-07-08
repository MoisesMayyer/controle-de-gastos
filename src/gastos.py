

lista_gastos = []
def adicionar_gastos():
    adicionar_gasto = {
        "nome_gasto": input("Digite o nome do gasto: "),
        "valor_gasto": float(input("Digite o valor do gasto: ")),
        "data": input("Digite a data do gasto (dd/mm/aaaa): ")
    }
    lista_gastos.append(adicionar_gasto)
    print("Gastos adicionados com sucesso!!")


def listar_gastos():
    print("Listando gastos")


def editar_gastos():
    print("Editar gastos")


def remover_gastos():
    print("Remover gastos")

def total_gastos():
    print("Total gastos")
