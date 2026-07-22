from dados.dados import carregar_json, salvar_json, CAMINHO_CATEGORIAS
#from financeiro.calculos import gasto_categoria
from utils.utils import criar_id

categorias_lista = carregar_json(CAMINHO_CATEGORIAS)


def nova_categoria():
    nome_categoria = input("Digite o nome da nova categoria: ")

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
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)

    id_remover = int(input("Qual você deseja remover: "))

    encontrada = False

    for categoria in categorias_lista:
        if categoria["id"] == id_remover:
            categorias_lista.remove(categoria)
            encontrada = True
            break

    if encontrada:
        salvar_json(CAMINHO_CATEGORIAS, categorias_lista)
        print("Categoria removida com sucesso!")
    else:
        print("Categoria não encontrada!")


def listar_categorias():
    categoria_lista = carregar_json(CAMINHO_CATEGORIAS)

    if not categoria_lista:
        print("Você deve criar uma categoria!")
        nova_categoria()


        categoria_lista = carregar_json(CAMINHO_CATEGORIAS)

    for categoria in categoria_lista:
        print(f"{categoria['id']} - {categoria['nome']}")

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
