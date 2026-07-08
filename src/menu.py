from gastos import (
    adicionar_gastos,
    listar_gastos,
    editar_gastos,
    remover_gastos,
    total_gastos,
)

def menu():
    print("="*5, "controle de gastos", "="*5)
    print(
        "1 - Adicionar gasto\n"
        "2 - Listar gastos\n"
        "3 - Editar gasto\n"
        "4 - Remover gasto\n"
        "5 - Total gasto\n"
        "6 - Sair"
    )
    
#menu temporário
def iniciar():
    while True:

        menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("opção invalida")
            print("Digite apenas números")
            continue

        if opcao == 1:
            adicionar_gastos()
        elif opcao == 2:
            listar_gastos()
        elif opcao == 3:
            editar_gastos()
        elif opcao == 4:
            remover_gastos()
        elif opcao == 5:
            total_gastos()
        else:
            break
