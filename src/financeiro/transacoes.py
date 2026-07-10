from dados.dados import salvar_json, carregar_json
from utils.utils import criar_id

lista_transacoes = carregar_json()

def adicionar_transacao():
    nome_gasto = input("Digite o nome do gasto: ")

    while True:
        try:
            valor_gasto = float(input("Digite o valor do gasto: "))
            break
        except ValueError:
            print("Valor inválido. Digite apenas números.")

    data_gasto = input("Digite a data do gasto (dd/mm/aaaa): ")

    gasto_id = criar_id(lista_transacoes)

    transacoes = {
        "id": gasto_id,
        "nome": nome_gasto,
        "valor": valor_gasto,
        "data": data_gasto
    }

    lista_transacoes.append(transacoes)
    salvar_json(lista_transacoes)
    print("Gasto adicionado com sucesso!")


def listar_gastos():
    carregar_json()
    if not lista_transacoes:
        print("Nenhum gasto registrado.")
        return

    for gasto in lista_transacoes:
        print(
            f"ID: {gasto['id']}\n"
            f"Nome: {gasto['nome']}\n"
            f"Valor: R$ {gasto['valor']:.2f}\n"
            f"Data: {gasto['data']}\n"
        )


def editar_gasto():
    if not lista_transacoes:
        print("Nenhum gasto registrado.")
        return

    while True:
        try:
            id_editar = int(input("Digite o ID que deseja editar: "))
            break
        except ValueError:
            print("digite um valor valido")

    for gasto in lista_transacoes:
        if gasto["id"] == id_editar:
            novo_nome = input("Digite o novo nome do gasto: ")

            while True:
                try:
                    novo_valor = float(input("Digite o novo valor do gasto: "))
                    break
                except ValueError:
                    print("Valor inválido. Digite apenas números.")

            nova_data = input("Digite a nova data do gasto (dd/mm/aaaa): ")

            gasto["nome"] = novo_nome
            gasto["valor"] = novo_valor
            gasto["data"] = nova_data
            salvar_json(lista_transacoes)

            print("Gasto editado com sucesso!")
            return

    print("Gasto não encontrado.")


def remover_gasto():
    if not lista_transacoes:
        print("Nenhum gasto registrado.")
        return

    while True:
        try:
            id_remover = int(input("Digite o ID que deseja remover: "))
            break
        except ValueError:
            print("Digite apenas números.")

    for gasto in lista_transacoes:
        if gasto["id"] == id_remover:
            lista_transacoes.remove(gasto)
            salvar_json(lista_transacoes)

            print("Gasto removido com sucesso!")
            return

    print("Gasto não encontrado.")


def total_gastos():
    if not lista_transacoes:
        print("Nenhum gasto registrado.")
        return

    soma_gastos = 0

    for gasto in lista_transacoes:
        soma_gastos += gasto['valor']

    print(f"Total gasto: R$ {soma_gastos:.2f}")