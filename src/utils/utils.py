

def criar_id(lista_transacoes):
    if not lista_transacoes:
        return 1

    return max(gasto["id"] for gasto in lista_transacoes) + 1
