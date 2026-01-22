from tasks import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa, listar_listas, nova_lista
from storage import salvar_tarefas, carregar_tarefas

def menu1():
    print("\n--- TO DO LIST ---")
    print("1 - Criar nova lista")
    print("2 - Acessar listas")
    print("3 - Sair")
    
def menu2():
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

def main():
    dicionario = carregar_tarefas()
    while True:
        menu1()
        opcao = input("\nEscolha uma das opções: ")
        if opcao == "1":
            nome_lista = input("Digite o nome da lista de tarefas que você deseja criar: ")
            if nova_lista(nome_lista, dicionario):
                print("Sua lista foi criada com sucesso!")
                salvar_tarefas(dicionario)
            else:
                print("Essa lista já existe, escolha outro nome!")
        elif opcao == "2":
            while True:
                listas = listar_listas(dicionario)
                if not listas:
                    print("Nenhuma lista encontrada.")
                    break
                print("Suas listas:")
                for nome in listas:
                    print(nome)
                escolha = input("\nDigite o nome da lista que você deseja acessar: ")
                if escolha in listas:
                    lista_escolhida = escolha
                    while True:
                        print(f"\n--- {lista_escolhida} ---")
                        menu2()
                        opcao = input("\nEscolha uma das opções: ")
                        if opcao == "1":
                            tarefa = input("Digite a tarefa que você deseja adicionar na lista: ")
                            if adicionar_tarefa(tarefa, lista_escolhida, dicionario):
                                print(f"A tarefa '{tarefa}' foi adicionada!")
                                salvar_tarefas(dicionario)
                        elif opcao == "2":
                            tarefas = listar_tarefas(lista_escolhida, dicionario)
                            if tarefas:
                                print(f"Tarefas da lista {lista_escolhida}:\n")
                                for t in tarefas:
                                    status = "✅" if t["concluida"] else "❌"
                                    print(f"{t['id']} {t['titulo']} - {status}")
                            else:
                                print("Essa lista não possui tarefas!")
                        elif opcao == "3":
                            try:
                                id_tarefa = int(input("Digite o ID da tarefa que você deseja concluir: "))
                                if concluir_tarefa(lista_escolhida, id_tarefa, dicionario):
                                    print("A tarefa foi concluída!")
                                    salvar_tarefas(dicionario)
                                else:
                                    print("ID não existe ou incorreto!")
                            except ValueError:
                                print("ID inválido!")
                        elif opcao == "4":
                            try:
                                id_tarefa = int(input("Digite o ID da tarefa que você deseja remover: "))
                                if remover_tarefa(lista_escolhida, id_tarefa, dicionario):
                                    print("A tarefa foi removida!")
                                    salvar_tarefas(dicionario)
                                else:
                                    print("ID não existe ou incorreto!")
                            except ValueError:
                                print("ID inválido!")
                        elif opcao == "5":
                            print("Saindo da lista...")
                            break
                        else:
                            print("Opção inválida!")
                    break
                else:
                    print("Lista não existe!")
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

main()
