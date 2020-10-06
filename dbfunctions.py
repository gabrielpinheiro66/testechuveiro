import mysql.connector

def altera_posicao(posicao):
    cnx = None
    func = None
    try:
        cnx = mysql.connector.connect(user='user', database='chaveiro', password='password', host='localhost', port='3306', connect_timeout=5)
        cursor = cnx.cursor()
        pos = (posicao,)
        query = "UPDATE engine SET position = %s"
        cursor.execute(query, (pos))
        cnx.commit()
        func = True
    except mysql.connector.Error as err:
            print("ERRO AO ATUALIZAR POSICAO")
            print("Nome do erro: {}".format(err))
            func = False
    finally:
        if cnx != None:
          cnx.close()
        return func

def confirmar(chave):
    cnx = None
    func = None
    try:
        cnx = mysql.connector.connect(user='user', database='chaveiro', password='password', host='localhost', port='3306', connect_timeout=5)
        cursor = cnx.cursor()
        chavea = (chave,)
        query = "UPDATE requisitions SET confirmed = true WHERE confirmed = false AND id_key = %s"
        cursor.execute(query, (chavea))
        cnx.commit()
        func = True
    except mysql.connector.Error as err:
            print("ERRO AO CONFIRMAR REQUISICAO")
            print("Nome do erro: {}".format(err))
            func = False
    finally:
        if cnx != None:
          cnx.close()
        return func

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

def le_posicao():
    cnx = None
    pos = None
    try:
        cnx = mysql.connector.connect(user='user', database='chaveiro', password='password', host='localhost', port='3306', connect_timeout=5)
        cursor = cnx.cursor()
        query = ("SELECT position FROM engine")
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
           pos = row[0]
    except mysql.connector.Error as err:
            print("ERRO AO LER POSICAO")
            print("Nome do erro: {}".format(err))
    finally:
        if cnx != None:
          cnx.close()
        return pos
