# Faça um programa que leia o comprimento do cateto oporto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

co = float(input('Digite o comprimento do Cateto Oposto:'))
ca = float(input('Digite o comprimento do Cateto Adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))
