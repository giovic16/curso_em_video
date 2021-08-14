# Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número:'))
un = num // 1 % 10
dz = num // 10 % 10
cn = num // 100 % 10
mi = num // 1000 % 10
print('Análisando o número {}'.format(num))
print('Unidade: {}'.format(un))
print('Dezena: {}'.format(dz))
print('Centena: {}'.format(cn))
print('Milhar: {}'.format(mi))



