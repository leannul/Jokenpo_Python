from emoji import emojize as e
from random import choice as c
from time import sleep

pedra = e(":raised_fist:")
papel = e(":hand_with_fingers_splayed:")
tesoura = e(":victory_hand:")

skills = [pedra,papel,tesoura]
enemy = e(c(skills))
title = 'JOKENPO GAME'

print(f'\033[1;35m{title:_^30}')

print('Selecione sua mão: ')

print(f'1- {pedra}')
print(f'2- {papel}')
print(f'3- {tesoura}')

opc = int(input('\033[1;34m'))
print('Processando...')
sleep(3)

#Sistema do jogo
if opc == 1:
    opc = pedra
elif opc == 2:
    opc = papel
elif opc == 3:
    opc = tesoura
else:
    print('Escolha uma das opções')

print(f'\033[1;33mSua mão: {opc}')
print(f'Mão do oponente: {enemy}')

#Quem vence ou perde
if opc in skills and enemy == opc:
    print('\033[1;36mEmpatado!!!')
elif opc == pedra and enemy == tesoura or opc == papel and enemy == pedra or opc == tesoura and enemy == papel:
    print('\033[1;32mVENCEU!!!')
else:
    print('\033[1;31mPERDEU!!')