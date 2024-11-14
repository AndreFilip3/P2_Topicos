import tkinter as tk

def tela_sobre():
    root = tk.Toplevel()
    root.title("Sobre")
    root.geometry("400x300")

    tk.Label(root, text="Sobre o Sistema", font=("Arial", 16)).pack(pady=20)
    tk.Label(root, text="Sistema de gerenciamento para loja de roupas.").pack(pady=10)
    tk.Label(root, text="Desenvolvedores:").pack(pady=10)
    tk.Label(root, text="• Ana Silva").pack()
    tk.Label(root, text="• João Souza").pack()

    root.mainloop()
