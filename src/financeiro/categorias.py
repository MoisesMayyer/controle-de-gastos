from dados.dados import carregar_json, salvar_json, CAMINHO_CATEGORIAS
from utils.utils import criar_id


def nova_categoria():
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)

    while True:
        nome_categoria = input("Digite o nome da nova categoria: ").strip()

        if nome_categoria:
            break

        print("O nome da categoria não pode ficar vazio.")

    while True:
        try:
            limite_categoria = float(input("Digite o limite da categoria: "))

            if limite_categoria < 0:
                print("O limite não pode ser negativo.")
                continue

            break

        except ValueError:
            print("Valor inválido. Digite apenas números.")

    id_categoria = criar_id(categorias_lista)

    categoria_nova = {
        "id": id_categoria,
        "nome": nome_categoria,
        "limite": limite_categoria
    }

    categorias_lista.append(categoria_nova)

    salvar_json(CAMINHO_CATEGORIAS, categorias_lista)

    print("Categoria adicionada com sucesso!")


def editar_categoria():
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)

    id_alterar = int(input("Digite o ID da categoria: "))

    for categoria in categorias_lista:
        if categoria["id"] == id_alterar:

            while True:
                novo_nome = input(
                    "Digite o novo nome da categoria: "
                ).strip()

                if novo_nome:
                    break

                print("O nome não pode ficar vazio.")

            while True:
                try:
                    novo_valor = float(
                        input("Digite o novo limite: ")
                    )

                    if novo_valor < 0:
                        print("O limite não pode ser negativo.")
                        continue

                    break

                except ValueError:
                    print("Digite um valor válido.")

            categoria["nome"] = novo_nome
            categoria["limite"] = novo_valor

            salvar_json(CAMINHO_CATEGORIAS, categorias_lista)

            print("Categoria alterada com sucesso!")
            return

    print("Categoria não encontrada!")


def remover_categoria():
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)

    id_remover = int(input("Qual categoria deseja remover? "))

    for categoria in categorias_lista:
        if categoria["id"] == id_remover:

            categorias_lista.remove(categoria)

            salvar_json(
                CAMINHO_CATEGORIAS,
                categorias_lista
            )

            print("Categoria removida com sucesso!")
            return

    print("Categoria não encontrada!")


def listar_categorias():
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)

    if not categorias_lista:
        print("Nenhuma categoria cadastrada.")
        return None

    print("\nCategorias disponíveis:")

    for categoria in categorias_lista:
        print(
            f"{categoria['id']} - {categoria['nome']}"
        )

    while True:
        try:
            id_categoria = int(
                input("Selecione o ID da categoria: ")
            )

        except ValueError:
            print("Digite apenas números.")
            continue

        existe = any(
            categoria["id"] == id_categoria
            for categoria in categorias_lista
        )

        if existe:
            return id_categoria

        print("Categoria não encontrada.")