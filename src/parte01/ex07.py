# ------
# Faça um Programa que peça o valor do lado de um quadrado e mostre a área e
# em seguida mostre o dobro desta área para o usuário.
# Dado: area = lado²
# ------
lado = float(input('Informe o lado do quadrado em centímetros: '))
area = lado ** 2
print(f'A Área do quadrado de lado {lado} é {area}. {2*area} é o dobro dessa área.')