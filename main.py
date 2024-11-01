# main.py
from database import inicializar_bd
from ui.login_ui import tela_login

def main():
    inicializar_bd()  # Inicializa as tabelas do banco de dados
    tela_login()  # Abre a interface de login

if __name__ == "__main__":
    main()