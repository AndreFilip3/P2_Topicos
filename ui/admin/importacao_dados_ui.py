import tkinter as tk
from tkinter import messagebox
from utils import importar_dados


def tela_importacao_dados():
    def importar():
        url = url_entry.get()
        if not url:
            messagebox.showerror("Erro", "A URL não pode estar vazia!")
            return

        try:
            importar_dados(url)
            messagebox.showinfo("Sucesso", "Dados importados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao importar dados: {e}")

    root = tk.Toplevel()
    root.title("Importação de Dados")
    root.geometry("400x300")

    tk.Label(root, text="Importar Dados", font=("Arial", 16)).pack(pady=20)

    tk.Label(root, text="URL para Importação:").pack()
    url_entry = tk.Entry(root)
    url_entry.pack(pady=10)

    tk.Button(root, text="Importar", command=importar).pack(pady=20)

    root.mainloop()
