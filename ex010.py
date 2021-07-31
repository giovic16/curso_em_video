# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Entre com seu saldo em R$'))
conv = real / 5.21
print('Com R${:.2f} você consegue comprar US${:.2f}' .format(real, conv))