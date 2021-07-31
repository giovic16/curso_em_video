# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugad
# o e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Informe por quantos dias você alugou o carro:'))
km = float(input('Digite a quantidade de Km percorrido:'))
total = (60 * d) + (km * 0.15)
print(f'O total a pagar é de R${total}')