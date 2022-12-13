from random import randint
from time import sleep
computador = randint(0, 5)
#print('~' * 20)
print('Vou tentar advinhar um número entre 0 a 5. Tente acertar...')
#print('~' * 20)
jogador = int(input('Que número eu pensei: '))
print('Processando...')
sleep(2)
if jogador == computador:
    print(' Acertouuuu!😄')
else:
    print(' Sinto muito, voce errou!😩 Eu pensei no número {}🤗'.format(computador, jogador))