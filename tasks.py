from storage import carregar_tarefas, salvar_tarefas

def adicionar_tarefa(task):
    tarefas = carregar_tarefas()
    if tarefas:
        novo_id = max(t["id"] for t in tarefas) + 1
    else:
        novo_id = 1

    tarefas.append({
        "id": novo_id,
        "titulo": task,
        "concluida": False
    })

    return tarefas


def listar_tarefas(lista):
    if len(lista) > 0:
        for tarefa in lista:
            if tarefa["concluida"]:
                status = "✅"
            else:
                status = "❌"
            print(tarefa["titulo"], "-", status)
    else:
        print("Você não possui nenhuma tarefa!")


def concluir_tarefa(lista, id_tarefa):
    i = 0
    while i < len(lista):
        if lista[i]["id"] == id_tarefa:
            lista[i]["concluida"] = True
            return lista
        i += 1
    print("ID não encontrado.")
    return lista
  

def remover_tarefa(lista, id_tarefa):
    x = 0
    while x < len(lista):
        if lista[x]["id"] == id_tarefa:
            lista.pop(x)
            return lista
        x += 1
    print("ID não encontrado.")
    return lista