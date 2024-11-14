import tkinter as tk
from tkinter import messagebox
from database import conectar

def tela_cadastro_usuario():
    def cadastrar():
        email = email_entry.get()
        senha = senha_entry.get()
        confirmar_senha = confirmar_senha_entry.get()

        if not email or not senha or not confirmar_senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não conferem!")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute("INSERT INTO usuarios (email, senha, is_admin) VALUES (?, ?, 0)", (email, senha))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            root.destroy()  # Fecha a tela de cadastro após o sucesso
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")
        finally:
            conexao.close()

    # Criação da janela
    root = tk.Toplevel()
    root.title("Cadastro de Usuário")
    root.geometry("400x300")

    tk.Label(root, text="Cadastro de Usuário", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="E-mail:").pack()
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    tk.Label(root, text="Senha:").pack()
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack(pady=5)

    tk.Label(root, text="Confirmar Senha:").pack()
    confirmar_senha_entry = tk.Entry(root, show="*")
    confirmar_senha_entry.pack(pady=5)

    tk.Button(root, text="Cadastrar", command=cadastrar, bg="#4CAF50", fg="white").pack(pady=20)

    root.mainloop()
