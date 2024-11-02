import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectando ao banco de dados SQLite
def conectar():
    conn = sqlite3.connect("usuarios.db")
    return conn

# Função para criar a tabela de usuários se não existir
def inicializar_bd():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            data_nascimento TEXT,
            usuario TEXT UNIQUE,
            senha TEXT
        )
    """)
    conn.commit()
    conn.close()

# Função para abrir a tela de cadastro
def abrir_tela_cadastro():
    # Criação da janela de cadastro
    cadastro = tk.Toplevel(janela_login)
    cadastro.title("Tela de Cadastro")
    cadastro.geometry("300x400")

    # Campo Nome Completo
    tk.Label(cadastro, text="Nome Completo:").pack(pady=5)
    entry_nome = tk.Entry(cadastro)
    entry_nome.pack(pady=5)

    # Campo Email
    tk.Label(cadastro, text="Email:").pack(pady=5)
    entry_email = tk.Entry(cadastro)
    entry_email.pack(pady=5)

    # Campo Telefone
    tk.Label(cadastro, text="Telefone:").pack(pady=5)
    entry_telefone = tk.Entry(cadastro)
    entry_telefone.pack(pady=5)

    # Campo Data de Nascimento
    tk.Label(cadastro, text="Data de Nascimento (DD/MM/AAAA):").pack(pady=5)
    entry_data_nascimento = tk.Entry(cadastro)
    entry_data_nascimento.pack(pady=5)

    # Campo Nome de Usuário
    tk.Label(cadastro, text="Nome de Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(cadastro)
    entry_usuario.pack(pady=5)

    # Campo Senha
    tk.Label(cadastro, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(cadastro, show="*")
    entry_senha.pack(pady=5)

    # Campo Confirmar Senha
    tk.Label(cadastro, text="Confirmar Senha:").pack(pady=5)
    entry_confirma_senha = tk.Entry(cadastro, show="*")
    entry_confirma_senha.pack(pady=5)

    # Função para cadastrar o usuário no banco de dados
    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        data_nascimento = entry_data_nascimento.get()
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        confirma_senha = entry_confirma_senha.get()

        if not (nome and email and telefone and data_nascimento and usuario and senha and confirma_senha):
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
            return

        if senha != confirma_senha:
            messagebox.showwarning("Atenção", "As senhas não coincidem!")
            return

        # Inserindo dados no banco de dados
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuarios (nome, email, telefone, data_nascimento, usuario, senha)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (nome, email, telefone, data_nascimento, usuario, senha))
            conn.commit()
            messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
            cadastro.destroy()  # Fecha a tela de cadastro após o sucesso
        except sqlite3.IntegrityError:
            messagebox.showwarning("Erro", "Nome de usuário já existente! Tente outro.")
        finally:
            conn.close()

    # Botão Cadastrar
    botao_cadastrar = tk.Button(cadastro, text="Cadastrar", command=cadastrar)
    botao_cadastrar.pack(pady=20)

# Função para realizar o login
def realizar_login():
    usuario = entry_usuario.get()
    senha = entry_senha_login.get()

    if not usuario or not senha:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
        return

    # Verificação no banco de dados
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    usuario_logado = cursor.fetchone()
    conn.close()

    if usuario_logado:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Usuário ou senha incorretos.")

# Criação da janela de login
janela_login = tk.Tk()
janela_login.title("Tela de Login")
janela_login.geometry("300x200")

# Inicializa o banco de dados e a tabela de usuários
inicializar_bd()

# Campo Usuário
tk.Label(janela_login, text="Usuário:").pack(pady=5)
entry_usuario = tk.Entry(janela_login)
entry_usuario.pack(pady=5)

# Campo Senha
tk.Label(janela_login, text="Senha:").pack(pady=5)
entry_senha_login = tk.Entry(janela_login, show="*")
entry_senha_login.pack(pady=5)

# Botão Login
botao_login = tk.Button(janela_login, text="Login", command=realizar_login)
botao_login.pack(pady=10)

# Botão para abrir a tela de cadastro
botao_cadastrar = tk.Button(janela_login, text="Cadastrar", command=abrir_tela_cadastro)
botao_cadastrar.pack(pady=5)

# Execução da janela principal
janela_login.mainloop()
