# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Digite o valor do produto R$'))
desc = v - (v * 5 / 100)
print('O valor do produto é R${} mas com a promoção de 5% de desconto o valor ficou R${:.2f}' .format(v, desc))
