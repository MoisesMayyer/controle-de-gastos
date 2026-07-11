

def criar_id(lista):
    if not lista:
        return 1

    return max(gasto["id"] for gasto in lista) + 1
