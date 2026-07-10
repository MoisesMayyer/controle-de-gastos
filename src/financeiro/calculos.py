from dados.dados import carregar_json

lista_transacoes = carregar_json()

def total_despesas():
    total = 0

    for transacao in lista_transacoes:
        if transacao["tipo"] == "despesa":
            total += transacao["valor"]

    return total


def total_receitas():
    total = 0

    for transacao in lista_transacoes:
        if transacao["tipo"] == "receita":
            total += transacao["valor"]

    return total


def saldo_atual():
    return total_receitas() - total_despesas()


def obter_resumo():
    transacoes = carregar_json()

    receitas = 0
    despesas = 0

    for transacao in transacoes:
        if transacao["tipo"] == "receita":
            receitas += transacao["valor"]

        elif transacao["tipo"] == "despesa":
            despesas += transacao["valor"]

    return {
        "saldo": receitas - despesas,
        "receitas": receitas,
        "despesas": despesas,
        "meta_economia": 1500,
        "economizado": 980
    }