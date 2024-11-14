import tkinter as tk
from ui.admin.pesquisa_cliente_ui import tela_pesquisa_cliente
from ui.admin.cadastro_produto_ui import tela_cadastro_produto
from ui.admin.pesquisa_produto_ui import tela_pesquisa_produto
from ui.admin.venda_ui import tela_vendas
from ui.admin.importacao_dados_ui import tela_importacao_dados
from ui.admin.exportacao_dados_ui import tela_exportacao_dados

def tela_menu_admin(usuario):
    root = tk.Tk()
    root.title("Menu do Administrador")
    root.geometry("600x600")

    tk.Label(root, text=f"Bem-vindo(a), Administrador {usuario['email']}!", font=("Arial", 16)).pack(pady=20)

    # Botões para funcionalidades administrativas
    tk.Button(root, text="Pesquisar Clientes", command=tela_pesquisa_cliente).pack(pady=10)
    tk.Button(root, text="Cadastrar Produtos", command=tela_cadastro_produto).pack(pady=10)
    tk.Button(root, text="Pesquisar Produtos", command=tela_pesquisa_produto).pack(pady=10)
    tk.Button(root, text="Histórico de Vendas", command=tela_vendas).pack(pady=10)
    tk.Button(root, text="Importar Dados", command=tela_importacao_dados).pack(pady=10)
    tk.Button(root, text="Exportar Dados", command=tela_exportacao_dados).pack(pady=10)

    tk.Button(root, text="Sair", command=root.destroy).pack(pady=20)

    root.mainloop()