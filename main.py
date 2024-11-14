from ui.login_ui import tela_login
from database import inicializar_bd

def main():
    # Inicializar banco de dados
    inicializar_bd()

    # Abrir tela de login
    tela_login()

if __name__ == "__main__":
    main()
