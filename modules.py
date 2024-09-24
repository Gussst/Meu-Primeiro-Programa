'''
Arquivo de Modulos
2024.08.13
Gustavo Maciel
'''


# --> Bibliotecas
from random import choice # importar choice da biblioteca random
from time import sleep
# --> Constantes, Variáveis e Listas
TAM = 50 # Tamanho da tela
CAR = choice(['=', '*', "|", "-"]) # Caracter utilizado para desenho 
MAR = 4 # Tamanho da Margem

# --> Funções
def clrScreen(): # Função para limpar a tela
  print('\n'*TAM) # Mostra na tela \n == Linha vazia * TAM

def displayLine(): # Função para mostrar uma linha de caracteres
  print(CAR*TAM) # Isso aqui é o que de fato vai fazer aparecer a linha, multiplicando as constantes

def displayMsg(msg): # Mostra uma msg alinhada a esquerda entre CAR
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}') # isso aqui de fato mostra a msg dentro da função

def displayMsgCenter(msg): # função para mostrar uma msg alinhada ao centro
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') # essa parte de fato cria a msg alinhada

def displayHeader(msgs): # isso aqui é a função para mostrar o cabeçalho
  displayLine() # chamando a função displayLine
  for item in msgs: # loop for para iterar dentro de msgs
    displayMsgCenter(item) # chama a função displayMsgCenter e coloca o parametro item
  displayLine() # chama novamente a função displayLine

def displayHeaderT(msgs): # isso aqui é a função para mostrar o cabeçalho
  displayLine() # chamando a função displayLine
  for item in msgs: # loop for para iterar dentro de msgs
    displayMsgCenter(item) # chama a função displayMsgCenter e coloca o parametro item
    sleep(1)
  displayLine()

def getUserOption(msg): # cria a função para obter a opção do usuário
  option = input(f'{CAR} {msg}: ').strip() # essa linha cria um input para receber a opção fornecida pelo usuário
  return option # isso retorna a opção

def validateUserOption(option, listOptions): # cria a função para validar a opção do usuário e passa os parametros option e listOptions
  if option in listOptions: # se a opção estiver em listOptions
    return True # retorna verdadeiro
  else: # caso falso
    msgsErro = ['Opção Inválida', 'Escolha Novamente....'] # lista com as msgs de erro
    displayHeader(msgsErro) # chama a função displayHeader e passa o parametro msgsErro
    return False # retorna falso


  
# --> Main