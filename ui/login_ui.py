import tkinter as tk
from tkinter import messagebox
from database import conectar
from ui.menu_ui import tela_menu
from ui.admin.menu_admin_ui import tela_menu_admin
from ui.cadastro_usuario_ui import tela_cadastro_usuario

def tela_login():
    def verificar_login():
        email = email_entry.get()
        senha = senha_entry.get()

        conexao = conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
            usuario = cursor.fetchone()

            if usuario:
                is_admin = usuario[3]
                if is_admin:
                    print("Login como administrador")
                    tela_menu_admin({"email": usuario[1]})  # Abre tela de admin
                else:
                    print("Login como usuário comum")
                    tela_menu({"email": usuario[1]})  # Abre tela de usuário comum
            else:
                messagebox.showerror("Erro", "E-mail ou senha inválidos!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        finally:
            conexao.close()

    # Criação da janela de login
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x300")

    tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=20)

    tk.Label(root, text="E-mail:").pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    tk.Label(root, text="Senha:").pack(pady=5)
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack(pady=5)

    tk.Button(root, text="Entrar", command=verificar_login, bg="#4CAF50", fg="white").pack(pady=20)
    tk.Button(root, text="Cadastrar", command=tela_cadastro_usuario).pack()

    root.mainloop()