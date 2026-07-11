from dados.dados import carregar_json, salvar_json, CAMINHO_CATEGORIAS
#from financeiro.calculos import gasto_categoria
from utils.utils import criar_id

categorias_lista = carregar_json(CAMINHO_CATEGORIAS)


def nova_categoria():
    nome_categoria = input("Digite o nome do categoria: ")

    while True:
        try:
            limite_categoria = float(input("Digite o limite da categoria: "))
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

    print("categoria adicionada com sucesso!")



def editar_limite():
    pass


def remover_categoria():
    pass


def listar_categorias():
    if categorias_lista:
        for categorias in categorias_lista:
            print(f"{categorias['id']} - {categorias['nome']}")
    else:
        print("Voce deve criar uma categoria!")
        nova_categoria()

    while True:
        id_categoria = int(input("Selecione o id da categoria: "))

        existe = any(
            categoria["id"] == id_categoria
            for categoria in categorias_lista
        )

        if not existe:
            print("Crie ou escolha uma categoria existente")
        else:
            return id_categoria
