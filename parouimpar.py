# Jogo de Par ou Ímpar
# 2024.08.20
# Gustavo Henrique Maciel

# --> Bibliotecas
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT # importa funções do modules
from random import randint # importa a função randint da biblioteca random
from time import sleep # importa a função sleep da biblioteca time

# --> Constantes, Variáveis e Listas
msgsInicio = ['Seja bem-vindo ao', 'Jogo de PAR OU ÍMPAR', 'Desenvolvido por: Gustavo Maciel', 'BOA SORTE!']  # Mensagens de início
playAgain = ''  # Variável para verificar se o jogador quer jogar novamente
playerScore = 0  # Pontuação do jogador
computerScore = 0  # Pontuação do computador

# --> Funções
def startParOuImpar(): # cria a função startParOuImpar
    global playerScore, computerScore  # Usa variáveis globais
    while True:  # Loop infinito para permitir várias rodadas
        playerScore = 0  # Reseta a pontuação do jogador
        computerScore = 0  # Reseta a pontuação do computador
        clrScreen()  # Limpa a tela
        displayHeader(msgsInicio)  # Exibe o cabeçalho de início

        while playerScore < 2 and computerScore < 2:  # Continua enquanto nenhum dos jogadores atingir 2 pontos
            # Pergunta ao jogador se quer "Par" ou "Ímpar"
            escolhaParOuImpar = getUserOption('Escolha Par ou Ímpar (P/I)').strip().upper()
            while escolhaParOuImpar not in ['P', 'I']:
                escolhaParOuImpar = getUserOption('Escolha Par ou Ímpar (P/I)').strip().upper()

            playParOuImpar(escolhaParOuImpar)  # Inicia o jogo com a escolha do jogador
            if playerScore >= 2 or computerScore >= 2:
                break  # Sai do loop se alguém alcançar 2 pontos

        # Exibe o placar final após o término do jogo
        displayScore("PLACAR FINAL", playerScore, computerScore)  # Mostra o placar final
        if playerScore > computerScore:
            displayHeader(['Parabéns', 'YOU WIN!'])  # Mostra mensagem de vitória se o jogador vencer
        else:
            displayHeader(['Parabéns', 'YOU LOSE!'])  # Mostra mensagem de derrota se o jogador perder

        # Pergunta se o jogador deseja jogar novamente
        playAgain = getUserOption('Deseja jogar novamente? [S/N]')  # Pergunta se o jogador deseja jogar novamente
        while not validateUserOption(playAgain, ['S', 'N', 's', 'n', 'y', 'Y']):  # Valida a resposta do usuário
            playAgain = getUserOption('Deseja jogar novamente? [S/N]')  # Repete a pergunta se a resposta for inválida
        if playAgain.lower() not in ['s', 'y']:  # Se a resposta não for 's' ou 'y', sai do loop
            break

def displayMenu():
    msgs = ["Escolha um número:"]
    displayLine()  # Exibe uma linha
    displayMsg(msgs[0])
    displayLine()  # Exibe uma linha

def displayScore(typeScore, playerScore, computerScore):
    msgs = []
    msgs.append(typeScore)  # Adiciona o tipo de placar à lista de mensagens
    msgs.append(f'Player: {playerScore} --- PC: {computerScore}')  # Adiciona o placar do jogador e do computador
    displayHeaderT(msgs)  # Mostra o placar

def determineWinner(playerChoice, computerChoice, escolhaParOuImpar):
    soma = playerChoice + computerChoice  # Calcula a soma dos números escolhidos
    resultado = 'P' if soma % 2 == 0 else 'I'  # Determina se a soma é Par ('P') ou Ímpar ('I')

    if escolhaParOuImpar == resultado:  # Verifica se a escolha do jogador corresponde ao resultado
        resultado_final = 'Você Ganhou!' #
    else:
        resultado_final = 'Você Perdeu!'

    msgs = [f'Você escolheu: {playerChoice}', f'O computador escolheu: {computerChoice}', f'A soma é {soma} ({resultado})', resultado_final]
    displayHeaderT(msgs)  # Exibe o resultado
    return resultado_final # retorna a variável

def playParOuImpar(escolhaParOuImpar):
    global playerScore, computerScore  # Usa variáveis globais
    while playerScore < 2 and computerScore < 2:  # Continua enquanto nenhum dos jogadores atingir 2 pontos
        displayMenu()  # Mostra o menu de opções
        try: # tente fazer isso
            playerChoice = int(getUserOption('Sua escolha'))  # Obtém a escolha do jogador
        except ValueError: # caso de um erro de entrada inválida
            displayMsg("Entrada inválida! Escolha um número válido.") # mostre essa msg
            continue # continua o código

        computerChoice = randint(0, 100)  # O computador escolhe um número aleatório (não há limite superior fixo)
        result = determineWinner(playerChoice, computerChoice, escolhaParOuImpar)  # Determina o vencedor
        if "Ganhou" in result: # condicional pra ver se aparece ganhou dentro de result
            playerScore += 1  # Incrementa a pontuação do jogador se ele ganhar
        elif "Perdeu" in result: # senão se está perdeu in result
            computerScore += 1  # Incrementa a pontuação do computador se ele ganhar
        if playerScore < 2 and computerScore < 2: # se essas variáveis forem menores que 2
            displayScore("PLACAR", playerScore, computerScore)  # Mostra o placar atual
        sleep(1)  # Pausa de 1 segundo



