from financeiro.transacoes import adicionar_transacao,remover_transacao,editar_transacao

def submenu_transacoes():
        while True:
            try:
                opcao = int(input("Digite sua opção: "))
            except ValueError:
                print("Opção inválida!")
                continue

            if opcao == 1:
                adicionar_transacao()

            elif opcao == 2:
                editar_transacao()

            elif opcao == 3:
                remover_transacao()

            elif opcao == 4:
                break

            else:
                print("Opção inexistente!")

