# Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('Digite um algo:')
print('Qual o tipo primitivo desse valor?', type(algo))
print('A entrada é um número?', algo.isnumeric())
print('A entrada é uma letra?', algo.isalpha())
print('A entrada é alfanumérica (letras e números)?', algo.isalnum())
print('A entrada possui somente letras maiúsculas?', algo.isupper())
print('A entrada possui somente letras minúsculas?', algo.islower())
print('A entrada possui espaços?', algo.isspace())
print('A entrada está capitalizada (maiúsculas e minúsculas)?', algo.istitle())