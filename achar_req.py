import mysql.connector

def le_requisicoes():
    cnx = None
    vetor = []
    try:
        cnx = mysql.connector.connect(user='user', database='chaveiro', password='password', host='localhost', port='3306', connect_timeout=5)
        cursor = cnx.cursor()
        query = ("SELECT id_key FROM requisitions WHERE confirmed = false")
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
           vetor.append(row[0])
    except mysql.connector.Error as err:
            print("ERRO AO LER REQUISICOES")
            print("Nome do erro: {}".format(err))
    finally:
        if cnx != None:
          cnx.close()
        return vetor


x = le_requisicoes()

print(x[0])
