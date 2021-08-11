# Tipos de Fatiamento:
frase = 'Curso em Video Python'  # 0 a 20 caracteres (contando com os espaços)
print(frase[9])  # identifica o caracter 9, no caso a letra "V"
print(frase[9:13])  # mostra desde o caracter 9 até o 13, excluindo o caracter do 13, no caso fica a palavra "Vide"
print(frase[9:21])  # mostra de 9 até 20, ignorando o 21 inexistente
print(frase[9:21:2])  # começa no 9, indo até o 20 pulando de 2 em 2
print(frase[:5])  # começa do caracter 0 indo até o caracter 4, excluindo o caracter 5
print(frase[15:])  # começa do caracter 15 e vai até o final, 20 no caso
print(frase[9::3])  # começa do caracter 9 e vai até o caracter 20, pulando de 3 em 3

# Análise
len(frase)  # esse comando mostra a quantidade de caracteres que a frase possui
frase.count('o')  # esse comando mostra quantas vezes a letra 'o' aparece na frase
frase.count('o', 0, 13)  # esse comando mostra quantas vezes a letra 'o' aparece na frase desde o 0 até o 12, eliminado o 13
frase.find('deo')  # esse comando mostra quantas vezes encontrou o 'deo', mostrando a posição que esses caracteres iniciaram
frase.find('Android')  # quando um caracter não é encontrado na frase, o programa mostrará ao usuário o valor de -1
# 'Curso' in frase # se existe esse caracter na frase o programa mostrará o valor "True"

# Transformação
frase.replace('Python', 'Android')  # o código irá substituir a palavra Python por Android
frase.upper()  # os caracteres ficarão em maiusculo
frase.lower()  # os caracteres ficarão em minusculo
frase.title()  # Coloca todas as palavras com a primeira letra em maiusculo
frase.capitalize()  # coloca todos os caracteres em minusculo e apenas a primeira letra fica em maiusculo
frase.strip()  # remove todos os espaços inuteis
frase.rstrip()  # remove somente os ultimos espaços inuteis
frase.strip()  # remove somente os primeiros espaços inuteis

# Divisão
frase.split() # divide a frase, colocando cada palavra em listas diferentes

# Junção
'-'.join(frase) # junta todos os elementos de frase utilizando hifen como separador


