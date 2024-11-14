import tkinter as tk
from ui.sobre_ui import tela_sobre
from ui.carrinho_ui import tela_carrinho

def tela_menu(usuario):
    root = tk.Tk()
    root.title("Menu - Loja de Roupas")
    root.geometry("600x400")

    tk.Label(root, text=f"Bem-vindo(a), {usuario['email']}!", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Carrinho", command=tela_carrinho).pack(pady=10)
    tk.Button(root, text="Sobre", command=tela_sobre).pack(pady=10)
    tk.Button(root, text="Sair", command=root.destroy).pack(pady=10)

    root.mainloop()
