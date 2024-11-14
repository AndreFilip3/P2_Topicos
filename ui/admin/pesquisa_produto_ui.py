import tkinter as tk
from database import conectar

def tela_pesquisa_produto():
    def buscar_produto():
        descricao = descricao_entry.get()
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos WHERE descricao LIKE ?", (f"%{descricao}%",))
        produtos = cursor.fetchall()
        conexao.close()

        for widget in resultados_frame.winfo_children():
            widget.destroy()

        for produto in produtos:
            tk.Label(resultados_frame, text=f"ID: {produto[0]}, Descrição: {produto[1]}, Preço: R${produto[2]:.2f}, Estoque: {produto[3]}").pack()

    root = tk.Toplevel()
    root.title("Pesquisa de Produtos")
    root.geometry("500x500")

    tk.Label(root, text="Pesquisa de Produtos", font=("Arial", 16)).pack(pady=20)

    tk.Label(root, text="Descrição:").pack()
    descricao_entry = tk.Entry(root)
    descricao_entry.pack(pady=5)

    tk.Button(root, text="Buscar", command=buscar_produto).pack(pady=10)

    resultados_frame = tk.Frame(root)
    resultados_frame.pack(pady=10, fill="both", expand=True)

    root.mainloop()
