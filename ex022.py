# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras tem (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome em maiúsculas:', nome.upper())
print('Seu nome em minúsculas:', nome.lower())
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
letras = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(letras[0])))