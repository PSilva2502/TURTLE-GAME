from turtle import Turtle

t = Turtle()

t.speed(1)

def Andar_frente():
  frente = int(input('Qual distancia a percorrer: '))
  t.forward(frente)

def Andar_tras():
  tras = int(input('Qual distancia a percorrer: '))
  t.backward(tras)

def Girar_direita():
  giro_direita = int(input('Quantos graus quer girar: '))
  t.left(giro_direita)

def Girar_esquerda():
  giro_esquerda = int(input('Quantos graus quer girar: '))
  t.right(giro_esquerda)

#Menu Principal

while True:
  print('\n1 - Andar para frente')
  print('2 - Andar para tras')
  print('3 - Girar para esquerda')
  print('4 - Girar para direita')
  print('5 - SAIR')
  
  opcao = int(input('Escolha uma opção: '))

  if opcao == 1:
    Andar_frente()
  elif opcao == 2:
    Andar_tras()
  elif opcao == 3:
    Girar_direita()
  elif opcao == 4:
    Girar_esquerda()
  elif opcao == 5:
    print('Saindo...')
    break
  else:
    print('Opção inválida')