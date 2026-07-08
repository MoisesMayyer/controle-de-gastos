

lista_gastos = []
def adicionar_gastos():
    nome_gasto = input("Digite o nome do gasto: ")

    while True:
        try:
            valor_gasto = float(input("Digite o valor do gasto: "))
            break
        except ValueError:
            print("Valor inválido. Digite apenas números.")

    data_gasto = input("Digite a data do gasto (dd/mm/aaaa): ")

    gasto = {
        "nome": nome_gasto,
        "valor": valor_gasto,
        "data": data_gasto
    }

    lista_gastos.append(gasto)
    print("Gasto adicionado com sucesso!")


def listar_gastos():
    if lista_gastos:
        for gasto in lista_gastos:
            print(
            f"Nome: {gasto['nome']}\n"
            f"Valor: {gasto['valor']:.2f}\n"
            f"Data: {gasto['data']}\n"
            )
    else:
        print("Nenhum gasto registrado.")


def editar_gastos():
    print("Editar gastos")


def remover_gastos():
    print("Remover gastos")

def total_gastos():
    print("Total gastos")
