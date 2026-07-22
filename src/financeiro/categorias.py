from dados.dados import carregar_json, salvar_json, CAMINHO_CATEGORIAS
from utils.utils import criar_id


def nova_categoria(nome_categoria, limite_categoria):
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)
    id_categoria = criar_id(categorias_lista)
    categoria_nova = {
        "id": id_categoria,
        "nome": nome_categoria,
        "limite": limite_categoria
    }
    categorias_lista.append(categoria_nova)
    salvar_json(CAMINHO_CATEGORIAS, categorias_lista)
    return True


def editar_categoria(id_alterar, novo_nome, novo_valor):
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)
    for categoria in categorias_lista:
        if categoria["id"] == id_alterar:
            categoria["nome"] = novo_nome
            categoria["limite"] = novo_valor
            salvar_json(CAMINHO_CATEGORIAS, categorias_lista)
            return True
    return False


def remover_categoria(id_remover):
    categorias_lista = carregar_json(CAMINHO_CATEGORIAS)
    for categoria in categorias_lista:
        if categoria["id"] == id_remover:
            categorias_lista.remove(categoria)
            salvar_json(CAMINHO_CATEGORIAS, categorias_lista)
            return True
    return False


def obter_todas_categorias():
    return carregar_json(CAMINHO_CATEGORIAS)