import tkinter as tk
from tkinter import messagebox
from database import conectar

def tela_cadastro_usuario():
    def cadastrar():
        # Obter os valores dos campos
        nome = nome_entry.get()
        sobrenome = sobrenome_entry.get()
        data_nascimento = data_nascimento_entry.get()
        telefone = telefone_entry.get()
        endereco = endereco_entry.get()
        email = email_entry.get()
        senha = senha_entry.get()
        confirmacao_senha = confirmacao_senha_entry.get()

        # Validações básicas
        if not all([nome, sobrenome, data_nascimento, telefone, endereco, email, senha, confirmacao_senha]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        if senha != confirmacao_senha:
            messagebox.showerror("Erro", "As senhas não conferem!")
            return

        try:
            conexao = conectar()
            cursor = conexao.cursor()

            # Inserir o usuário no banco de dados como um usuário comum
            cursor.execute("""
            INSERT INTO usuarios (nome, sobrenome, data_nascimento, telefone, endereco, email, senha, is_admin)
            VALUES (?, ?, ?, ?, ?, ?, ?, 0)
            """, (nome, sobrenome, data_nascimento, telefone, endereco, email, senha))
            conexao.commit()
            conexao.close()

            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            root.destroy()  # Fecha a tela de cadastro após o sucesso
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    # Criação da janela de cadastro
    root = tk.Toplevel()
    root.title("Cadastro de Usuário")
    root.geometry("400x500")

    tk.Label(root, text="Cadastro de Usuário", font=("Arial", 16)).pack(pady=10)

    # Campos do formulário
    tk.Label(root, text="Nome:").pack()
    nome_entry = tk.Entry(root)
    nome_entry.pack(pady=5)

    tk.Label(root, text="Sobrenome:").pack()
    sobrenome_entry = tk.Entry(root)
    sobrenome_entry.pack(pady=5)

    tk.Label(root, text="Data de Nascimento (DD/MM/AAAA):").pack()
    data_nascimento_entry = tk.Entry(root)
    data_nascimento_entry.pack(pady=5)

    tk.Label(root, text="Telefone:").pack()
    telefone_entry = tk.Entry(root)
    telefone_entry.pack(pady=5)

    tk.Label(root, text="Endereço:").pack()
    endereco_entry = tk.Entry(root)
    endereco_entry.pack(pady=5)

    tk.Label(root, text="E-mail:").pack()
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    tk.Label(root, text="Senha:").pack()
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack(pady=5)

    tk.Label(root, text="Confirmação de Senha:").pack()
    confirmacao_senha_entry = tk.Entry(root, show="*")
    confirmacao_senha_entry.pack(pady=5)

    # Botão para enviar o cadastro
    tk.Button(root, text="Cadastrar", command=cadastrar, bg="#4CAF50", fg="white").pack(pady=20)

    root.mainloop()