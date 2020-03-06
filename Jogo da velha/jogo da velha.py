from random import randint #importa a funçao randint do random

def mostra_tabuleiro(tabuleiro):
    '''
    Imprime o tabuleiro na tela
    '''
    print("     A  |  B  |  C\n")
    print(" 1   %s  |  %s  |  %s "%(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("  --------------------\n 2   %s  |  %s  |  %s "%(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("  --------------------\n 3   %s  |  %s  |  %s \n"%(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))
    return


def constroi_velha():
    '''
    Cria o tabuleiro vazio do jogo
    '''
    
    tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    return tabuleiro

def atualiza_tabuleiro(movimento,tabuleiro,jogador):
    '''
    Recebe a jogada a atualiza o tabuleiro
    '''
    
    coluna = movimento[0]
    linha = movimento[1].upper()
    
    if coluna == '1':
        coluna = 0
    elif coluna == '2':
        coluna = 1
    elif coluna == '3':
        coluna = 2
    if linha == 'A':
        linha = 0
    elif linha == 'B':
        linha = 1
    elif linha == 'C':
        linha = 2

    if tabuleiro[coluna][linha] == ' ':
        tabuleiro[coluna][linha] = jogador
        jogada_pc(tabuleiro,jogador)
    else:
        print("Casa ja ocupada selecione outra")
        jogar(tabuleiro,jogador)
    



def jogada_pc(tabuleiro,jogador):
    '''
    faz o pc realizar uma jogada
    '''
    pc = ' '
    while True:
        linha = randint(0,2) # seleciona um numero inteiro pseudoaleatorio dentre 0 e 2
        coluna = randint(0,2)
        if tabuleiro[linha][coluna] == ' ':
            break
        else: continue
    if jogador == 'X':
        pc = 'O'
    elif jogador == 'O':
        pc = 'X'
    tabuleiro[linha][coluna] = pc
    mostra_tabuleiro(tabuleiro)
    verifica_fim(tabuleiro,jogador)
    jogar(tabuleiro,jogador)


def resultado(tabuleiro,ganhador,jogador):
    '''
    Apresenta o final do jogo
    '''
    if ganhador == jogador:
        print("Parabens voce ganhou!!!")
        exit()
    else:
        print("Que pena tente outra vez")
        exit()
    
        

def verifica_fim(tabuleiro,jogador):
    '''
    verifica se o jogo chegou ao fim
    '''
    op = 0
    while op < 2:
        if op == 0 :
            jog = 'X'
        elif op == 1 :
            jog = 'O'
        if tabuleiro[0][0] == jog and tabuleiro[0][1] == jog and tabuleiro[0][2] == jog:
            resultado(tabuleiro,tabuleiro[0][0],jogador)
        elif tabuleiro[0][0] == jog and tabuleiro[1][0] == jog and tabuleiro[2][0] == jog:
            resultado(tabuleiro,tabuleiro[0][0],jogador)
        elif tabuleiro[1][0] == jog and tabuleiro[1][1] == jog and tabuleiro[1][2] == jog:
            resultado(tabuleiro,tabuleiro[1][0],jogador)
        elif tabuleiro[2][0] == jog and tabuleiro[2][1] == jog and tabuleiro[2][2] == jog:
            resultado(tabuleiro,tabuleiro[2][0],jogador)
        elif tabuleiro[0][1] == jog and tabuleiro[1][1] == jog and tabuleiro[2][1] == jog:
            resultado(tabuleiro,tabuleiro[1][1],jogador)
        elif tabuleiro[0][2] == jog and tabuleiro[1][2] == jog and tabuleiro[2][2] == jog:
            resultado(tabuleiro,tabuleiro[1][2],jogador)
        elif tabuleiro[0][0] == jog and tabuleiro[1][1] == jog and tabuleiro[2][2] == jog:
            resultado(tabuleiro,tabuleiro[1][1],jogador)
        elif tabuleiro[0][2] == jog and tabuleiro[1][1] == jog and tabuleiro[2][0] == jog:
            resultado(tabuleiro,tabuleiro[1][1],jogador)
        op+=1
 
    
        
    return
    
def jogar(tabuleiro,jogador):
    '''
    Realiza a jogada
    '''
    print("Se precisar de ajuda digite h")
    movimento = input("Digite a sua jogada: ")
    if movimento.upper() == 'H':
        exemplo()
        
    if len(movimento) == 2:
        coluna = movimento[0]
        linha = movimento[1].upper()
    else:
        print("Voce escolheu uma opçao invalida jogue novamente")
        jogar(tabuleiro,jogador)
        
    if coluna == '1' or coluna == '2' or coluna == '3' :
        if linha == 'A' or linha == 'B' or linha == 'C':
            atualiza_tabuleiro(movimento,tabuleiro,jogador)
        else:
            print("Voce escolheu uma opçao invalida jogue novamente")
            jogar(tabuleiro,jogador)
    else:
        print("Voce escolheu uma opçao invalida jogue novamente")
        jogar(tabuleiro,jogador)
    



def exemplo():
    '''
    Explica como efetuar a jogada para o jogador
    '''
    print("#####REGRAS#####\n    Vence o jogador que tiver suas peças em sequencia\n    Para realizar a jogada deve se escolher um numero e uma letra"
          " \n    exemplo: 1a ou 3b \n    Nunca a letra na frente do numero ou numeros e letras que nao sao apresentado no tabuleiro")
    return
    

def main():
    '''
    Tela principal do jogo
    '''
    print("###JOGO DA VELHA###")
    while True:
        jogador = input("Voce quer ser o X ou o O?: ")
        if jogador.upper() == 'X' or jogador.upper() == 'O':
            tabuleiro = constroi_velha()
            mostra_tabuleiro(tabuleiro)
            jogar(tabuleiro,jogador.upper())
            break
        elif jogador == 1:
            exit()
        else:
            print("Favor selecione X ou O ou digite 1 para sair")


main()

        
