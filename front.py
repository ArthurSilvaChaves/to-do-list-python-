import customtkinter as ctk
import json
import back

loadarquivos = back.loaddados()

def main():
    mainscreen = ctk.CTk()
    

    mainscreen.mainloop()

def createaccont():
    createaccontscreen =  ctk.CTk()
    createaccontscreen.geometry("300x200")
    createaccontscreen.title("Create Account")
    createaccontscreen.resizable(False,False)

    usuario = ctk.CTkEntry(createaccontscreen,font=("Consolas",16),placeholder_text="Usuário",width=200)
    usuario.pack(pady=5)

    senha = ctk.CTkEntry(createaccontscreen,font=("Consolas",16),placeholder_text="Senha",width=200)
    senha.pack(pady=5)

    criarcontabtn = ctk.CTkEntry(createaccontscreen,text="Criar Conta",font=("Calibri",16))
    criarcontabtn.pack(pady=5)

    createaccontscreen.mainloop()