# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Digite a largura da parede:'))
h = float(input('Digite a altura da parede:'))
calc = l * h
print(
    'Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(l, h, calc), "\n"
    f'Para pintar essa parede, você precisará de {calc/2}l de tinta.')
