import tkinter as tk
from database import conectar

def tela_pesquisa_cliente():
    def buscar_cliente():
        email = email_entry.get()
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email LIKE ?", (f"%{email}%",))
        clientes = cursor.fetchall()
        conexao.close()

        for widget in resultados_frame.winfo_children():
            widget.destroy()

        for cliente in clientes:
            tk.Label(resultados_frame, text=f"ID: {cliente[0]}, E-mail: {cliente[1]}").pack()

    root = tk.Toplevel()
    root.title("Pesquisa de Clientes")
    root.geometry("400x400")

    tk.Label(root, text="Pesquisa de Clientes", font=("Arial", 16)).pack(pady=20)

    tk.Label(root, text="E-mail:").pack()
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    tk.Button(root, text="Buscar", command=buscar_cliente).pack(pady=10)

    resultados_frame = tk.Frame(root)
    resultados_frame.pack(pady=10, fill="both", expand=True)

    root.mainloop()
