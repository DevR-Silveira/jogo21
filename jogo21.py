from random import randint
from time import sleep

# Flags do Jogo
jogo = True
chave = False
# Contadores do Jogo
contador = vitoria = empate = derrota = quebra = 0

while jogo == True: # Primeiro While: Repete o laço do jogo inteiro até que o jogador não queira.
    # Restart
    if contador >= 1:
        jogardnv = input('Deseja jogar de novo? [S/N] ').strip().upper()[0]
        if jogardnv == 'S':
            chave = False
            pass
        elif jogardnv == 'N':
            break
        else:
            print('Dado Inválido')
    # Deck Computador
    carta1c = randint(1, 11)
    carta2c = randint(1, 11)
    deckc = [carta1c, carta2c]
    # Deck Jogador
    carta1j = randint(1, 11)
    carta2j = randint(1, 11)
    deckj = [carta1j, carta2j]
    # Carta de Hit
    carta3 = ''
    # Total Computador e Jogador
    totc = carta1c + carta2c
    totj = carta1j + carta2j
    while True: # Segundo While: Enquanto verdadeiro, repete o laço
        # Restart de apoio
        if contador >= 1 and chave == True:
            break 
        else:
            pass
        # Display Jogador
        print('-=' * 15)
        print(f'Deck Jogador: {deckj}')
        print(f'Total: {totj}')
        print('-=' * 15)
        print('[ 1 ] HIT [ 2 ] STAND') # Menu
        escolha = int(input('Sua escolha: ')) # Input do Menu
        sleep(1) # O programa dorme por 1seg, apenas para efeito visual.
        if escolha == 1: # Se escolher HIT será adicionada mais uma carta ao seu deck
            carta3 = randint(1, 11)
            deckj.append(carta3) # Adiciona a nova carta ao Deck do Jogador
            totj += carta3 # Aumenta o total a cada carta acrescentada
            print(f'Veio um {carta3}. Total: {totj}')
            if totj > 21:
                print('Você estourou a banca.')
                print('Você perdeu.')
                print('-=' * 15)
                contador += 1
                quebra += 1
                derrota += 1
                break
        elif escolha == 2: # Jogador fica com o Deck escolhido, e computador começa a escolher suas cartas
            print(f'Você fica com esse deck: {deckj}')
            print('Vez do computador')
            sleep(1)
            while totc > 0: # Terceiro While: Enquanto o total do PC for maior a 0, ou seja verdadeiro, continue.
                # Display PC
                print('-=' * 15)
                print(f'Deck Computador: {deckc}')
                print(f'Total: {totc}')
                print('-=' * 15)
                sleep(2)
                # Acrescenta mais uma carta ao deck do computador, até que uma condição seja verdadeira.
                carta3 = randint(1, 11)
                totc += carta3
                deckc.append(carta3)
                if totc <= 21 and totc >= 18: # Stand do Computador
                    print('-=' * 15)
                    print(f'Deck Computador: {deckc}')
                    print(f'Total: {totc}')
                    print('-=' * 15)
                    sleep(2)
                    if totj > totc: # Se o total do jogador for maior que o Computador, ele ganha.
                        print(f'Seu Deck: {deckj} Total: {totj}')
                        print(f'É maior que o Deck do computador: {deckc} Total: {totc}')
                        print('Você Ganhou.')
                        print('-=' * 15)
                        vitoria += 1
                        contador += 1
                        chave = True
                        break
                    elif totj == totc: # Se for igual, empata.
                        print(f'Seu Deck: {deckj} Total: {totj}')
                        print(f'É igual ao Deck do computador: {deckc} Total: {totc}')
                        print('Empate')
                        print('-=' * 15)
                        contador += 1
                        empate += 1
                        chave = True
                        break
                    else: # Se for menor, ele perde.
                        print(f'Seu Deck: {deckj} Total: {totj}')
                        print(f'É menor que o Deck do computador: {deckc} Total: {totc}')
                        print('Você perdeu.')
                        print('-=' * 15)
                        contador += 1
                        derrota += 1
                        chave = True
                        break
                elif totc > 21: # Se o computador passar o total de 21, o jogador ganha.
                    print('-=' * 15)
                    print(f'Deck Computador: {deckc}')
                    print(f'Total: {totc}')
                    print('-=' * 15)
                    print('Computador Estourou a Banca.')
                    print('Você Ganhou.')
                    print('-=' * 15)
                    contador += 1
                    quebra += 1
                    vitoria += 1
                    chave = True
                    break
        else:
            print('Dado Inválido. Tente Novamente.')
print('===' * 15)
print('ESTATÍSTICAS DAS PARTIDAS:')
print(f'''Números de Partidas: {contador}
Vitórias: {vitoria}
Empates: {empate}
Derrotas: {derrota}
A banca já estourou {quebra} vezes.''')
print('===' * 15)
print('===== FIM DE PROGRAMA =====')
