import json
import sqlite3
from database import conectar

def exportar_dados_json():
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
    print("Dados exportados para dados.json com sucesso.")
