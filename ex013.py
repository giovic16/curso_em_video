# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite seu atual salário R$'))
aum = s + (s * 15 / 100)
print('O seu atual salário é de R${}, com o reajuste de 15% ficou R${:.2f}' .format(s, aum))
