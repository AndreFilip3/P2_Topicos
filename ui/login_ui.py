# ui/login_ui.py
import tkinter as tk
from tkinter import messagebox
from database import conectar

def login_usuario(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome=? AND senha=?", (nome, senha))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario

def tela_login():
    def autenticar():
        nome = entry_nome.get()
        senha = entry_senha.get()
        if login_usuario(nome, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            janela.destroy()
            # Chame a função para abrir o menu principal
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    janela = tk.Tk()
    janela.title("Login")

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Senha:").pack()
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack()

    tk.Button(janela, text="Login", command=autenticar).pack()
    janela.mainloop()