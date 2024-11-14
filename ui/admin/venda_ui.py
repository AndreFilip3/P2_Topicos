import tkinter as tk
from tkinter import messagebox
from database import conectar
from utils import exportar_dados_json

def tela_vendas():
    def listar_vendas():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        SELECT v.id, p.descricao, v.quantidade, v.total, v.data
        FROM vendas v
        JOIN produtos p ON v.produto_id = p.id
        """)
        vendas = cursor.fetchall()
        conexao.close()

        for widget in resultados_frame.winfo_children():
            widget.destroy()

        for venda in vendas:
            tk.Label(resultados_frame, text=f"ID: {venda[0]}, Produto: {venda[1]}, Quantidade: {venda[2]}, Total: R${venda[3]:.2f}, Data: {venda[4]}").pack()

    def exportar_relatorio():
        exportar_dados_json()
        messagebox.showinfo("Exportação", "Relatório exportado para 'dados.json'.")

    root = tk.Toplevel()
    root.title("Vendas")
    root.geometry("600x600")

    tk.Label(root, text="Histórico de Vendas", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Listar Vendas", command=listar_vendas).pack(pady=10)
    tk.Button(root, text="Exportar Relatório", command=exportar_relatorio).pack(pady=10)

    resultados_frame = tk.Frame(root)
    resultados_frame.pack(pady=10, fill="both", expand=True)

    root.mainloop()
