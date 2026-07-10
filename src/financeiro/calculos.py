from dados.dados import carregar_json


def total_despesas():
    transacoes = carregar_json()

    total = 0

    for t in transacoes:
        if t["tipo"] == "despesa":
            total += t["valor"]

    return total


def total_receitas():
    transacoes = carregar_json()

    total = 0

    for t in transacoes:
        if t["tipo"] == "receita":
            total += t["valor"]

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