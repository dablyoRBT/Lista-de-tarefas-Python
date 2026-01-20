def adicionar_tarefa (lista, task):
    maior_id = max(i["id"] for i in lista) # foi muito dificil pegar esse id n sei oq fazer tive que pesquisar
    lista.append({"id": maior_id + 1, "titulo": task, "concluida": False})
    return lista
    

def listar_tarefas(lista):
    for tarefa in lista:
        if tarefa["concluida"]:
            status = "✅"
        else:
            status = "❌"
        print(tarefa["titulo"], "-", status)


def concluir_tarefa(lista, id_tarefa):
    i = 0
    while i < len(lista):
        if lista[i]["id"] == id_tarefa:
            lista[i]["concluida"] = True
            return True
        i += 1
    return False

        
        
def remover_tarefa(lista, id_tarefa):
    i = 0
    while i < len(lista):
        if lista[i]["id"] == id_tarefa:
            lista.pop(i)
            return lista
        else:
            i += 1
    return False