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
    return {
        "saldo": saldo_atual(),
        "receitas": total_receitas(),
        "despesas": total_despesas(),
        "meta_economia": 1500.00,
        "economizado": 980.00,
    }