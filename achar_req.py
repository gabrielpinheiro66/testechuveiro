import mysql.connector

def le_requisicoes():
    cnx = None
    try:
        cnx = mysql.connector.connect(user='user', database='chaveiro', password='password', host='localhost', port='3306', connect_timeout=5)
        cursor = cnx.cursor()
        query = ("SELECT confirmed FROM requisitions")
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        print()
        print("----------------")
        for row in records:
            vetor = row
    except mysql.connector.Error as err:
            print("ERRO AO LER REQUISICOES")
            print("Nome do erro: {}".format(err))
    finally:
        if cnx != None:
          cnx.close()
        return vetor


print(le_requisicoes())
