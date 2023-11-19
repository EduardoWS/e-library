import sqlite3

def imprimir_registros():
    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')

    # Criar um cursor
    cursor = conn.cursor()

    # Executar uma consulta para obter todos os registros da tabela "livros"
    cursor.execute("SELECT * FROM livros")

    # Obter todos os resultados da consulta
    registros = cursor.fetchall()

    # Imprimir os resultados
    for registro in registros:
        print(registro)

    # Fechar a conexão
    conn.close()

# Chamar a função para imprimir os registros
imprimir_registros()