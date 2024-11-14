import json
import requests

def exportar_dados_json():
    from database import conectar  # Importe somente dentro da função para evitar ciclo

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        dados = {
            "usuarios": cursor.execute("SELECT * FROM usuarios").fetchall(),
            "produtos": cursor.execute("SELECT * FROM produtos").fetchall(),
            "vendas": cursor.execute("SELECT * FROM vendas").fetchall(),
        }
        conexao.close()

        with open("dados.json", "w") as json_file:
            json.dump(dados, json_file, indent=4)

        print("Dados exportados com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")

def importar_dados(url):
    from database import conectar  # Importe somente dentro da função para evitar ciclo

    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Erro ao acessar URL: {response.status_code}")

        dados = response.json()
        conexao = conectar()
        cursor = conexao.cursor()

        # Importar usuários
        for usuario in dados.get("usuarios", []):
            cursor.execute("""
                INSERT OR IGNORE INTO usuarios (id, email, senha, is_admin)
                VALUES (?, ?, ?, ?)
            """, (usuario["id"], usuario["email"], usuario["senha"], usuario["is_admin"]))

        # Importar produtos
        for produto in dados.get("produtos", []):
            cursor.execute("""
                INSERT OR IGNORE INTO produtos (id, codigo, descricao, preco, estoque)
                VALUES (?, ?, ?, ?, ?)
            """, (produto["id"], produto["codigo"], produto["descricao"], produto["preco"], produto["estoque"]))

        conexao.commit()
        conexao.close()

        print("Dados importados com sucesso!")
    except Exception as e:
        print(f"Erro ao importar dados: {e}")
