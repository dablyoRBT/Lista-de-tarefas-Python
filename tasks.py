def nova_lista(nome_lista, dados):
    if nome_lista in dados:
        return False 
    dados[nome_lista] = []
    return True

def adicionar_tarefa(task, lista_escolhida, dados):
    if lista_escolhida not in dados:
        return False
    if dados[lista_escolhida]:
        novo_id = max(t["id"] for t in dados[lista_escolhida]) + 1
    else:
        novo_id = 1
    dados[lista_escolhida].append({
        "id": novo_id,
        "titulo": task,
        "concluida": False
    })
    return True


def listar_tarefas(lista_escolhida, dados):
    if lista_escolhida not in dados:
        return None
    return dados[lista_escolhida]


def concluir_tarefa(lista_escolhida, id_tarefa, dados):
    for tarefa in dados[lista_escolhida]:
        if tarefa["id"] == id_tarefa:
            tarefa["concluida"] = True
            return True
    return False

def remover_tarefa(lista_escolhida, id_tarefa, dados):
    for i, tarefa in enumerate(dados[lista_escolhida]):
        if tarefa["id"] == id_tarefa:
            dados[lista_escolhida].pop(i)
            return True
    return False


def listar_listas(dados):
    return list(dados.keys())


