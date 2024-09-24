'''
Jogo do Pedra-Papel-Tesoura
2024.08.13
Gustavo Henrique Maciel
'''

# Bibliotecas
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeader, displayHeaderT # importa de modules as funções
from random import randint
from time import sleep
#Constantes, Variáveis, Listas
msgsInicio = ['Seja bem vindo ao', 'Jogo do PEDRA-PAPEL-TESOURA', 'Desenvolvido por: Gustavo Maciel', 'BOA SORTE!'] # lista com as msgs de inicio
msgs = []
playAgain = '' # variável vazia
playerScore = 0
computerScore = 0


#Funções
def startPPT(): # função que será usada para iniciar o jogo
  while(True): # loop while infinito
    clrScreen() # chama a função que limpa a tela
    displayHeader(msgsInicio) # chama a função displayHeader e passa o parametro msgsInicio
    # função para começar o jogo
    playPPT()
    playAgain = getUserOption('Deseja jogar novamente? [S/N]') # atribui um input com mensagem para a variável playAgain
    while not validateUserOption(playAgain, ['S', 'N', 's', 'n', 'y','Y']): # loop while para validar a opção do usuário
      playAgain = getUserOption('Deseja jogar novamente? [S/N]') # atribui um input com mensagem para a variável playAgain
    if playAgain.lower() != 's' or playAgain.lower() != 'y': # se a opção for diferente de s ou y
      break # para o loop while




def displayMenu():
  msgs = ["Escolha:", "[0] --> Pedra", '[1] --> Papel', "[2] --> Tesoura"]
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()



def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)
  
  





def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate'
  elif (playerChoice == '0' and computerChoice == '2') or \
       (playerChoice == '1' and computerChoice == '0') or \
       (playerChoice == '2' and computerChoice == '1'):
    play = f"{playerChoiceStr} vence {computerChoiceStr}"
    result = 'Você Ganhou!'
  else:
    play = f"{computerChoiceStr} vence {playerChoiceStr}"
    result = "Você Perdeu!"
  msgs = ['Jogada do Player: ' + playerChoiceStr, 'Jogada do PC: ' + computerChoiceStr, play, result]
  displayHeaderT(msgs)
  return result




  
def playPPT():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0', '1', '2']):
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice)
    if "Ganhou" in result:
      playerScore += 1
    elif "Perdeu" in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore("PLACAR", playerScore, computerScore)
    sleep(1)
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns', 'YOU WIN!'])
  else:
    displayHeader(['Parabéns', 'YOU LOSE!'])
# Main