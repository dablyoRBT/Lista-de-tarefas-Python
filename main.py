from tasks import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa

Tarefas = []

def menu():
    print("\n--- TO DO LIST ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")

def main():
    menu()
    while True:
        opcoes = ("1", "2", "3", "4", "0")
        opcao = input("Escolha uma das opções: ")
        if opcao in opcoes:
            match opcao:
                case "1":
                    Tarefa = input(f"Digite a tarefa que você deseja adicionar na lista: ")
                    adicionar_tarefa(Tarefas, Tarefa)
                    print(f"A tarefa {Tarefa} foi adicionada na sua lista!")
                    break
                case "2":
                    listar_tarefas(Tarefas)
                    break
                case "3":
                    id_tarefa = input("Digite o ID da tarefa que você deseja concluir: ") 
                    concluir_tarefa(Tarefas, id_tarefa)
                    print(f"A tarefa {Tarefa} foi concluida!")
                    break
                case "4":
                    id_tarefa = input(f"Digite o ID da tarefa que você deseja remover da lista: ") 
                    concluir_tarefa(Tarefas, id_tarefa)
                    (f"A tarefa {Tarefa} foi removida na sua lista!")
                    break
                case "0":
                    print("Fim do programa!")
                    break
        else:
            print("Opção inválida!")
            continue
            


main()
