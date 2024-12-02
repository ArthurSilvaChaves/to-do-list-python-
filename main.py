import json
from InquirerPy import inquirer

def loaddados(arquivo):
    try:
        with open(arquivo,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"tarefas":[]}
    
def savetodo(arquivo,tarefas):
    with open(arquivo,"w") as f:
        json.dump(tarefas, f, ident=4)

def menu():
    choices = inquirer.select(
        message="escolha uma ação",
        choices=[
            {"name":"1. listar tarefas","value":1},
            {"name":"2. adicionar tarefas","value":2},
            {"name":"3. marcar tarefa como concluída","value":3},
            {"name":"4. remover tarefa","value":4},
            {"name":"5. sair","value":5}
        ]
    ).execute()
    return choices

def main():
    arquivo = "tarefas.json"
    tarefas = loaddados(arquivo)
    
    while True:
        opcao = menu()
        match opcao:
            case 1:
                print("você escolheu a primeira opção")
            case 2:
                print("você escolheu a segunda opção")
            case 3:
                print("você escolheu a terceira opção")
            case 4:
                print("você escolheu a quarta opção")
            case 5:
                print("saindo...")
                break

if __name__ == "__main__":
    main()