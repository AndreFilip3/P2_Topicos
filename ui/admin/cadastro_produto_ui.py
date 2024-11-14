import tkinter as tk
from database import conectar

def tela_cadastro_produto():
    def salvar_produto():
        codigo = codigo_entry.get()
        descricao = descricao_entry.get()
        preco = preco_entry.get()
        estoque = estoque_entry.get()

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (codigo, descricao, preco, estoque) VALUES (?, ?, ?, ?)",
            (codigo, descricao, float(preco), int(estoque))
        )
        conexao.commit()
        conexao.close()

        tk.messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

    root = tk.Toplevel()
    root.title("Cadastro de Produtos")
    root.geometry("400x400")

    tk.Label(root, text="Código:").pack(pady=5)
    codigo_entry = tk.Entry(root)
    codigo_entry.pack(pady=5)

    tk.Label(root, text="Descrição:").pack(pady=5)
    descricao_entry = tk.Entry(root)
    descricao_entry.pack(pady=5)

    tk.Label(root, text="Preço:").pack(pady=5)
    preco_entry = tk.Entry(root)
    preco_entry.pack(pady=5)

    tk.Label(root, text="Estoque:").pack(pady=5)
    estoque_entry = tk.Entry(root)
    estoque_entry.pack(pady=5)

    tk.Button(root, text="Salvar", command=salvar_produto).pack(pady=20)

    root.mainloop()
