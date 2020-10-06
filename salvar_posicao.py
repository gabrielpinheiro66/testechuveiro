
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

posicao = 35

x = altera_posicao(posicao)

if(x):
  print("Deu bom")
else:
  print("Nao deu")
