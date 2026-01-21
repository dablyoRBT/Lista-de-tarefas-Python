from tasks import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa
from storage import salvar_tarefas, carregar_tarefas

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
        Tarefas = carregar_tarefas()
        opcoes = ("1", "2", "3", "4", "0")
        opcao = input("Escolha uma das opções: ")
        if opcao in opcoes:
            match opcao:
                case "1":
                    Tarefa = input(f"Digite a tarefa que você deseja adicionar na lista: ")
                    update = adicionar_tarefa(Tarefa)
                    print(f"A tarefa {Tarefa} foi adicionada na sua lista!")
                    salvar_tarefas(update)
                    continue
                case "2":
                    listar_tarefas(Tarefas)
                    continue
                case "3":
                    id_tarefa = int(input("Digite o ID da tarefa que você deseja concluir: "))
                    update = concluir_tarefa(Tarefas, id_tarefa)
                    print("A tarefa foi concluida!")
                    salvar_tarefas(update)
                    continue
                case "4":
                    id_tarefa = int(input(f"Digite o ID da tarefa que você deseja remover da lista: "))
                    update = remover_tarefa(Tarefas, id_tarefa)
                    print("A tarefa foi removida na sua lista!")
                    salvar_tarefas(update)
                    continue
                case "0":
                    print("Fim do programa!")
                    break
        else:
            print("Opção inválida!")
            continue
            
main()
