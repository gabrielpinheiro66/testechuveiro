import mysql.connector

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
            print("ERRO AO ATUALIZAR SALDO")
            print("Nome do erro: {}".format(err))
            func = False
    finally:
        if cnx != None:
          cnx.close()
        return func
