# ------
# Faça um programa que peça um número natural e mostre a tabuada de
# multiplicar(1 a 10) desse número.
# ------

print('Programa TABUADA')
num = int(input('Informe um número inteiro: '))
for i in range(10):
    print(f'{i+1} * {num} = {(i+1)*num}')