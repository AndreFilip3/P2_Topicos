import tkinter as tk
from tkinter import messagebox
from database import conectar
from ui.menu_ui import tela_menu
from ui.cadastro_usuario_ui import tela_cadastro_usuario

def tela_login():
    def verificar_login():
        email = email_entry.get()
        senha = senha_entry.get()

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()
        conexao.close()

        if usuario:
            tela_menu({"email": email, "is_admin": usuario[3]})
        else:
            messagebox.showerror("Erro", "E-mail ou senha inválidos!")

    root = tk.Tk()
    root.title("Login")
    root.geometry("400x200")

    tk.Label(root, text="E-mail:").pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    tk.Label(root, text="Senha:").pack(pady=5)
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack(pady=5)

    tk.Button(root, text="Login", command=verificar_login).pack(pady=20)
    tk.Button(root, text="Cadastrar", command=tela_cadastro_usuario).pack()

    root.mainloop()
