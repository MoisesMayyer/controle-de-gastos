

def criar_id(lista_gastos):
    if not lista_gastos:
        return 1

    return max(gasto["id"] for gasto in lista_gastos) + 1
