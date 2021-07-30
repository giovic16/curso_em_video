# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt

num = int(input('Digite um número:'))
d = num*2
t = num*3
r = sqrt(num)
print('O dobro de {} é {}' .format(num, d))
print('O triplo de {} é {}' .format(num, t))
print('A raiz quadrada de {} é igual a {:.2f}' .format(num, r))
