import json
import customtkinter as ctk
import front

def loaddados():
    arquivo = "tarefas.json"

    try:
        with open(arquivo,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"usuarios":[]}
    
def savetodo(arquivo,dados):
    with open(arquivo,"w") as f:
        json.dump(dados, f, indent=4)

def listtodo(tarefas): 
    if not tarefas["tarefas"]:
        print("\nnenhuma tarefa atribuida")
    else:
        for i,tarefa in enumerate(tarefas["tarefas"],start=1):
            status = "✔️" if tarefa["status"] == "concluida" else "❌"
            print(f"{i}. {tarefa['nome']} - {status}")

def addtodo(tarefas): 
    nome = input("Digite o nome da tarefa: ")
    if nome:
        tarefas["tarefas"].append({"nome": nome, "status": "pendente"})
        print(f"Tarefa '{nome}' adicionada com sucesso!")
    else:
        print("escreva alguma coisa no campo")

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
    listtodo(tarefas)
    try:
        indice = int(input("numero da  tarefa que será apagada: ")) - 1
        if 0 <= indice < len(tarefas["tarefas"]):
            removida = tarefas["tarefas"].pop(indice)
            print(f"tarefa '{removida['nome']}' removida")
        else:
            print("numero invalido")
    except ValueError:
        print("entrada invalida")

def login():
    def verilogin():
        usuario = usuarioent.get()
        senha = senhaent.get()
        dados = loaddados()


        if usuario in dados["usuarios"] and dados["usuarios"][usuario]["senha"] == senha:
            loginscreen.destroy()
            front.main()
        else:
            pass
    
    ctk.set_default_color_theme("green")
    
    loginscreen = ctk.CTk()
    loginscreen.title("Login")
    loginscreen.geometry("300x200")
    loginscreen.resizable(False,False)

    usuarioent = ctk.CTkEntry(loginscreen,placeholder_text="Usuário",font=("Consolas",16),width=200)
    usuarioent.pack(pady=5)

    senhaent = ctk.CTkEntry(loginscreen,placeholder_text="Senha",font=("Consolas",16),width=200)
    senhaent.pack(pady=5)

    loginbtn = ctk.CTkButton(loginscreen,text="Entrar",font=("Calibri",16),command=verilogin)
    loginbtn.pack(pady=5)

    createaccontbtn = ctk.CTkButton(loginscreen,text="Criar Conta",font=("Calibri",16))
    createaccontbtn.pack(pady=5)

    loginscreen.mainloop()

if __name__ == "__main__":
    login()