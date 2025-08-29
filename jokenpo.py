#Jokenpô
import random
from time import sleep

#Introdução e esolha do usuario.
print('Escolha: PEDRA, PAPEL OU TESOURA!')
usua = str(input('Qual deseja escolher? ')).strip().upper()

#Lista com opções
joke = ['PEDRA', 'PAPEL', 'TESOURA']

#jokenpo
print('---' * 13)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('---' * 13)

#Escolha da maquina
maquina = random.choice(joke)
print('-=' * 13)
print(f'Você jogou: {usua}.')
print(f'Python jogou: {maquina}.')
print('-=' * 13)

#Condições
if usua == maquina:
    print(f"Empate! Ambos jogaram {usua}.")
elif (usua == "PEDRA" and maquina == "TESOURA") or (usua == "PAPEL" and maquina == "PEDRA") or (usua == "TESOURA" and maquina == "PAPEL"):
    print("Você VENCEU!!! ")
else:
    print("O Python venceu! ")
