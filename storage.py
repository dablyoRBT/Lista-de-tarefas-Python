import json

def salvar_tarefas(colecao):
    ARQUIVO = "storage.json"
    arquivo = open(ARQUIVO, 'w')
    arquivo.write(json.dumps(colecao)) #Conversão para json
    arquivo.close()

def carregar_tarefas():
    ARQUIVO = "storage.json"
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo) #Lê o json e retorna a lista python novamente
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []

