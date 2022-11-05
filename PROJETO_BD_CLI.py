import sqlite3
from sqlite3 import Error

def conexao():
    caminho = "Bancos/Banco.db"
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)

sql_insert = 'INSERT INTO cliente VALUES (2, "luiz.silva", "acre");'
sql_remover = 'DELETE FROM cliente WHERE id = 2;'
sql_atualizar = 'UPDATE cliente SET usuário= "Luiz" WHERE id = 1'
sql_consultar = 'SELECT  * FROM cliente;'

def remover(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    except Error as er:
        print(er)

def inserir(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    except Error as er:
         print(er)

def atualizar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    except Error as er:
        print(er)

def consultar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    except Error as er:
        print(er)

