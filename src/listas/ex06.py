# ------
# Faça um Programa que peça o raio de um círculo, em centímetros, calcule e
# mostre sua área em centímetros quadrados.
# Dado: PI = 3.14 e A = PI * raio²
# ------
PI = 3.14
raio = float(input('Informe o raio do círculo em centímetros: '))
area = PI * raio ** 2
print(f'A área de um círculo de raio {raio} é {area}')