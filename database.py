# database.py
import sqlite3

def conectar():
    return sqlite3.connect("loja_de_roupa.db")

def inicializar_bd():
    conexao = conectar()
    cursor = conexao.cursor()

    # Criação de tabelas: exemplo com três tabelas principais
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        senha TEXT NOT NULL
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL,
                        estoque INTEGER
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        produto_id INTEGER,
                        quantidade INTEGER,
                        total REAL,
                        data TEXT,
                        FOREIGN KEY (produto_id) REFERENCES produtos(id)
                      )''')

    conexao.commit()
    conexao.close()