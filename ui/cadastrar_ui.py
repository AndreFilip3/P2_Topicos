import tkinter as tk
from tkinter import messagebox


def cadastrar():
    # Obtenha os valores dos campos de entrada
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    data_nascimento = entry_data_nascimento.get()
    senha = entry_senha.get()
    confirma_senha = entry_confirma_senha.get()
    
    # Verifique se todos os campos estão preenchidos
    if not (nome and email and telefone and data_nascimento and senha and confirma_senha):
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
        return
    
    # Verifique se as senhas coincidem
    if senha != confirma_senha:
        messagebox.showwarning("Atenção", "As senhas não coincidem!")
        return
    
    # Se tudo estiver certo, exiba uma mensagem de sucesso
    messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
    
    # Limpa os campos após o cadastro
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_data_nascimento.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_confirma_senha.delete(0, tk.END)


# Criação da janela principal
janela = tk.Tk()
janela.title("Tela de Cadastro")
janela.geometry("300x400")

# Campo Nome Completo
tk.Label(janela, text="Nome Completo:").pack(pady=5)
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=5)

# Campo Email
tk.Label(janela, text="Email:").pack(pady=5)
entry_email = tk.Entry(janela)
entry_email.pack(pady=5)

# Campo Telefone
tk.Label(janela, text="Telefone:").pack(pady=5)
entry_telefone = tk.Entry(janela)
entry_telefone.pack(pady=5)

# Campo Data de Nascimento
tk.Label(janela, text="Data de Nascimento (DD/MM/AAAA):").pack(pady=5)
entry_data_nascimento = tk.Entry(janela)
entry_data_nascimento.pack(pady=5)

# Campo Senha
tk.Label(janela, text="Senha:").pack(pady=5)
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)

# Campo Confirmar Senha
tk.Label(janela, text="Confirmar Senha:").pack(pady=5)
entry_confirma_senha = tk.Entry(janela, show="*")
entry_confirma_senha.pack(pady=5)

# Botão Cadastrar
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=20)

# Execução da janela
janela.mainloop()
