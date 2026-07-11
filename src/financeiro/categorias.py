from dados.dados import carregar_json, salvar_json, CAMINHO_CATEGORIAS

categorias_lista = carregar_json(CAMINHO_CATEGORIAS)


def nova_categoria():
    nome_categoria = input("Digite o nome do categoria: ")

    while True:
        try:
            limite_categoria = float(input("Digite o limite da categoria: "))
            break
        except ValueError:
            print("Valor inválido. Digite apenas números.")

    categoria_nova = {
        "categoria_id": "categoria_id",
        "nome": nome_categoria,
        "gasto": "gasto_categoria",
        "limite": limite_categoria
    }

    categorias_lista.append(categoria_nova)
    salvar_json(CAMINHO_CATEGORIAS, categorias_lista)

    print("categoria adicionada com sucesso!")


def editar_limite():
    pass


def remover_categoria():
    pass



