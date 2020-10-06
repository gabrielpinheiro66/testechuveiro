import RPi.GPIO as GPIO
import dbfunctions
import mfunctions
import time

print("Iniciou!")

state = 'inicial'
vetor = []
chave_desejada = None
posicao_atual = None
posicao_desejada = None
dir = None
tam = None



posicao_atual = dbfunctions.le_posicao()


while True:

    ## ESTADO INICIAL

    if state == 'inicial':
        print("Lendo requisicoes..........")
        vetor = dbfunctions.le_requisicoes()
        if len(vetor) > 0:
            state == 1
        time.sleep(0.01)

    ## ESTADO 1

    elif state == 1:
        chave_desejada = vetor[0]
        posicao_desejada = mfunctions.onde(chave_desejada)
        dir = mfunctions.lado(posicao_atual, posicao_desejada)

        tam = mfunctions.casas(posicao_atual, posicao_desejada)

        if dir: #horario
            for i in range(tam):
                mfunctions.passo_h()
                posicao_atual = mfunctions.andar_posicao_h(posicao_atual)
        elif not dir: #antihorario
            for i in range(tam):
                mfunctions.passo_ah()
                posicao_atual = mfunctions.andar_posicao_ah(posicao_atual)
        GPIO.cleanup()
        if (posicao_atual == posicao_desejada):
            dbfunctions.altera_posicao(posicao_atual)
            state = 2
        else:
            print("ERROU NO ROLE")
        time.sleep(0.01)
        state = 2

    ## ESTADO 2

    elif state == 2:
        a = input("Aperte o botao")
        dbfunctions.confirmar(chave_desejada)
        time.sleep(0.01)
        state = 3


    ## ESTADO 3

    elif state == 3:
        posicao_desejada = 0
        dir = mfunctions.lado(posicao_atual, posicao_desejada)
        tam = mfunctions.casas(posicao_atual, posicao_desejada)

        if dir: #horario
            for i in range(tam):
                mfunctions.passo_h()
                posicao_atual = mfunctions.andar_posicao_h(posicao_atual)
        elif not dir: #antihorario
            for i in range(tam):
                mfunctions.passo_ah()
                posicao_atual = mfunctions.andar_posicao_ah(posicao_atual)
        GPIO.cleanup()
        if (posicao_atual == posicao_desejada):
            dbfunctions.altera_posicao(posicao_atual)
            state = 'inicial'
        else:
            print("ERROU NO ROLE")
