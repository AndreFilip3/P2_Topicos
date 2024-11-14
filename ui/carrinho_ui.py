import tkinter as tk

def tela_carrinho():
    root = tk.Toplevel()
    root.title("Carrinho")
    root.geometry("400x300")

    tk.Label(root, text="Seu Carrinho", font=("Arial", 16)).pack(pady=20)

    tk.Label(root, text="Nenhum item no carrinho.").pack(pady=10)
    tk.Button(root, text="Fechar", command=root.destroy).pack(pady=20)

    root.mainloop()
