

def criar_id(lista_transacoes):
    if not lista_transacoes:
        return 1

    return max(gasto["id"] for gasto in lista_transacoes) + 1

def criar_id_categoria(lista_categorias):
    if not lista_categorias:
        return 1

    return max(gasto["categoria_id"] for gasto in lista_categorias) + 1