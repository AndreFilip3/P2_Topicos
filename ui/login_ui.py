# ui/login_ui.py
import tkinter as tk
from tkinter import messagebox
from database import conectar, inicializar_bd

# Função para autenticar usuário no banco de dados
def login_usuario(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome=? AND senha=?", (nome, senha))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario

# Função para abrir a tela de cadastro
def tela_cadastro():
    # Criação da janela de cadastro
    cadastro = tk.Toplevel()
    cadastro.title("Cadastro")
    cadastro.geometry("300x400")

    tk.Label(cadastro, text="Nome Completo:").pack(pady=5)
    entry_nome = tk.Entry(cadastro)
    entry_nome.pack(pady=5)

    tk.Label(cadastro, text="Email:").pack(pady=5)
    entry_email = tk.Entry(cadastro)
    entry_email.pack(pady=5)

    tk.Label(cadastro, text="Telefone:").pack(pady=5)
    entry_telefone = tk.Entry(cadastro)
    entry_telefone.pack(pady=5)

    tk.Label(cadastro, text="Data de Nascimento (DD/MM/AAAA):").pack(pady=5)
    entry_data_nascimento = tk.Entry(cadastro)
    entry_data_nascimento.pack(pady=5)

    tk.Label(cadastro, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(cadastro, show="*")
    entry_senha.pack(pady=5)

    tk.Label(cadastro, text="Confirmar Senha:").pack(pady=5)
    entry_confirma_senha = tk.Entry(cadastro, show="*")
    entry_confirma_senha.pack(pady=5)

    # Função para cadastrar novo usuário no banco de dados
    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        data_nascimento = entry_data_nascimento.get()
        senha = entry_senha.get()
        confirma_senha = entry_confirma_senha.get()

        if not (nome and email and telefone and data_nascimento and senha and confirma_senha):
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
            return

        if senha != confirma_senha:
            messagebox.showwarning("Atenção", "As senhas não coincidem!")
            return

        # Conexão com o banco de dados e inserção do novo usuário
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
        cadastro.destroy()  # Fecha a tela de cadastro após o sucesso

    # Botão Cadastrar
    tk.Button(cadastro, text="Cadastrar", command=cadastrar).pack(pady=20)

# Função para abrir a tela de login
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
    janela.geometry("300x200")

    tk.Label(janela, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.pack(pady=5)

    tk.Label(janela, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack(pady=5)

    tk.Button(janela, text="Login", command=autenticar).pack(pady=10)

    # Botão para abrir a tela de cadastro
    tk.Button(janela, text="Cadastrar", command=tela_cadastro).pack(pady=5)

    janela.mainloop()

# Inicialização do banco de dados ao iniciar o programa
if __name__ == "__main__":
    inicializar_bd()
    tela_login()
