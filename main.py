'''
Projeto Jogo Pedra-Papel-Tesoura
2024.08.13
Gustavo Maciel
'''

# --> Bibliotecas
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT # importa funções do arquivo modules.py
from ppt import startPPT # importa funções do arquivo ppt.py
from parouimpar import startParOuImpar
# --> Constantes, Variáveis e Listas
listaMsgs = ['oi', 'Esse é um', 'Teste', 'do Cabeçalho'] # uma lista para colocar palavras que do teste feito anteriormente
# --> Funções

# --> Main
def main():
  msgs = ['Seja Bem-vindo aos Jogos', 'PEDRA-PAPEL-TESOURA', 'PAR OU IMPAR']
  displayHeader(msgs)
  msgs = ['Digite 0 --> Sair', 'Digite 1 --> Pedra-Papel-Tesoura', 'Digite 2 -->   Par ou ímpar']
  displayHeaderT(msgs)
  opUser = getUserOption('Sua escolha')
  while not validateUserOption(opUser, ['0', '1', '2']):
    opUser = getUserOption('Sua escolha')
  if(opUser == '1'):
    startPPT() # Inicia o jogo
  elif(opUser == '2'):
    startParOuImpar()
  else:
    displayMsgCenter('Até a Próxima...')
  
  
  
  
  startPPT() # uma função para inicar o jogo
main()

