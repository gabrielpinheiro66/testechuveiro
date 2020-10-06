import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

def passo_h():
    for i in range(8):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

def passo_ah():
    for i in range(8):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[7-halfstep][pin])
            time.sleep(0.001)


def onde(chave):
    if (1<chave<15):
        return chave
    elif (16<chave<31):
        return chave+1
    elif (32<chave<47):
        return chave+2
    elif (48<chave<60):
        return chave+3
        
#false p antihorario
#true p horario

def lado(atual, pos):
    num = atual-pos
    if(num<0):
        if (num<-32):
            return False
        else:
            return True
    else:
        if(num<32):
            return False
        else:
            return True


def andar_posicao_h(posicao):
    if posicao == 63:
        posicao = 0
    else:
        posicao +=1
    return posicao

def andar_posicao_ah(posicao):
    if posicao == 0:
        posicao = 63
    else:
        posicao -=1
    return posicao

def casas(atual, pos):
    num = abs(atual-pos)
    if (num<32):
        return num
    else:
        return 64-num
