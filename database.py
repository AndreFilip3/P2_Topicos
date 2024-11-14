import sqlite3

def conectar():
    return sqlite3.connect("loja_de_roupa.db")

def inicializar_bd():
    conexao = conectar()
    cursor = conexao.cursor()

    # Atualização da tabela de usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        telefone TEXT NOT NULL,
        endereco TEXT NOT NULL,
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

def criar_admin():
    conexao = conectar()
    cursor = conexao.cursor()

    # Criação do administrador com e-mail e senha predefinidos
    try:
        cursor.execute("""
        INSERT OR IGNORE INTO usuarios (email, senha, is_admin)
        VALUES ('admin@loja.com', 'admin123', 1)
        """)
        conexao.commit()
        print("Usuário administrador criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar administrador: {e}")
    finally:
        conexao.close()

if __name__ == "__main__":
    inicializar_bd()
    criar_admin()
