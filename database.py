import sqlite3

def conectar():
    return sqlite3.connect("loja_de_roupa.db")

def inicializar_bd():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        is_admin INTEGER DEFAULT 0
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL UNIQUE,
        descricao TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        total REAL NOT NULL,
        data TEXT NOT NULL,
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    );
    ''')

    conexao.commit()
    conexao.close()
