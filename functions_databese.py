import sqlite3


def conectar():
    return sqlite3.connect('sistema_doacao.db') # Conexao com o Banco.

def criar_tabelas():
    #Chamamos a conexão e criamos as tabelas 
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS doadores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_doador TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    peso REAL,
                    tipo_sanguineo TEXT NOT NULL,
                    status TEXT
                   )
                   ''')
    conexao.commit()
    conexao.close()


def cadastrar_doador(nome_doador, idade , peso , tipo_sanguineo, status):
    #Recebe os dados da pessoa e grava no banco
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO doadores(nome_doador , idade , peso ,tipo_sanguineo, status)
        VALUES(?, ?, ?, ?,?)
         ''', (nome_doador, idade, peso , tipo_sanguineo, status))
    conexao.commit()
    conexao.close()


def buscar_doadores():
    #Exibe a lista de todos os doadores para exibir no menu
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM doadores')
    '''O fetchall retorna uma lista de tuplas, onde cada tupla representa uma linha do banco de dados'''
    doadores = cursor.fetchall()
    conexao.close()
    return doadores



def deletar_doador(id_doador):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM doadores WHERE id = ?" , (id_doador, ))
    conexao.commit()
    conexao.close()
