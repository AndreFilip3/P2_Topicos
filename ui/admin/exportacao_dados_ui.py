import tkinter as tk
from tkinter import messagebox
from utils import exportar_dados_json

def tela_exportacao_dados():
    def exportar():
        exportar_dados_json()
        messagebox.showinfo("Exportação", "Dados exportados com sucesso para 'dados.json'.")

    root = tk.Toplevel()
    root.title("Exportação de Dados")
    root.geometry("400x200")

    tk.Label(root, text="Exportar Dados", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Exportar para JSON", command=exportar).pack(pady=20)

    root.mainloop()
