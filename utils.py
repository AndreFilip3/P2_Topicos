# utils.py
import json
import sqlite3
import zipfile

def exportar_dados_json():
    conexao = sqlite3.connect("loja_de_roupa.db")
    cursor = conexao.cursor()

    dados = {
        "usuarios": cursor.execute("SELECT * FROM usuarios").fetchall(),
        "produtos": cursor.execute("SELECT * FROM produtos").fetchall(),
        "vendas": cursor.execute("SELECT * FROM vendas").fetchall(),
    }

    conexao.close()

    with open("dados.json", "w") as json_file:
        json.dump(dados, json_file, indent=4)

    with zipfile.ZipFile("dados.zip", "w") as zip_file:
        zip_file.write("dados.json")

    print("Dados exportados para dados.zip")

# utils.py (continuação)
import requests

def importar_dados(url):
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()

        conexao = sqlite3.connect("loja_de_roupa.db")
        cursor = conexao.cursor()
        
        # Exemplo de importação de produtos (modifique conforme necessário)
        for produto in dados.get("produtos", []):
            cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)",
                           (produto["nome"], produto["preco"], produto["estoque"]))

        conexao.commit()
        conexao.close()
        print("Dados importados com sucesso.")
    else:
        print("Erro ao importar dados.")