# ui/menu_ui.py
import tkinter as tk
from tkinter import messagebox
from ui import cadastro_produto_ui  # Exemplo de outra UI

def abrir_menu_principal():
    janela = tk.Tk()
    janela.title("Menu Principal")

    tk.Label(janela, text="Menu Principal").pack()
    
    tk.Button(janela, text="Cadastro de Produto", command=cadastro_produto_ui.cadastro_produto).pack()
    # Adicione mais botões para outras funcionalidades

    janela.mainloop()