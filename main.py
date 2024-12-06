import json
from InquirerPy import inquirer
import os

def loaddados(arquivo):
    try:
        with open(arquivo,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"tarefas":[]}
    
def savetodo(arquivo,tarefas):
    with open(arquivo,"w") as f:
        json.dump(tarefas, f, indent=4)

def menu():
    choices = inquirer.select(
        message="escolha uma ação",
        choices=[
            {"name":"1. listar tarefas","value":1},
            {"name":"2. adicionar tarefas","value":2},
            {"name":"3. marcar tarefa como concluída","value":3},
            {"name":"4. remover tarefa","value":4},
            {"name":"5. sair","value":5},
            {"name":"6. Sair sem salvar","value":6}
        ]).execute()
    return choices

def listtodo(tarefas): 
    if not tarefas["tarefas"]:
        print("\nnenhuma tarefa atribuida")
    else:
        for i,tarefa in enumerate(tarefas["tarefas"],start=1):
            status = "✔️" if tarefa["status"] == "concluida" else "❌"
            print(f"{i}. {tarefa['nome']} - {status}")

def addtodo(tarefas): 
    nome = input("Digite o nome da tarefa: ")
    tarefas["tarefas"].append({"nome": nome, "status": "pendente"})
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def marktodo(tarefas): 
    listtodo(tarefas)
    try:
        indice = int(input("\nDigite o número da tarefa para concluir: ")) - 1
        if 0 <= indice < len(tarefas["tarefas"]):
            tarefas["tarefas"][indice]["status"] = "concluida"
            print("tarefa marcada")
        else:
            print("numero invalido")
    except ValueError:
        print("entrada invalida")

def removetodo(tarefas): 
    pass

def main():
    arquivo = "tarefas.json"
    tarefas = loaddados(arquivo)
    
    while True:
        opcao = menu()
        match opcao:
            case 1:      
                os.system("cls")
                listtodo(tarefas)
            case 2:
                os.system("cls")
                addtodo(tarefas)
            case 3:
                os.system("cls")
                marktodo(tarefas)
            case 4:
                os.system("cls")
                print("você escolheu a quarta opção")
            case 5:
                os.system("cls")
                savetodo(arquivo,tarefas)
                print("saindo...")
                break
            case 6:
                os.system("cls")
                yorn = inquirer.select(
                    message="tem certeza que quer sair sem salvar?",
                    choices=[
                        {"name":"Sim","value":True},
                        {"name":"Não","value":False}
                    ]
                ).execute()

                if yorn:
                    os.system("cls")
                    print("Saindo...")
                    break
                else:
                    os.system("cls")
                    pass

if __name__ == "__main__":
    main()