# --------------------
# Lista 01
# Arquivo: parte01/ex04.py
# Autor: mweb - pythonisk team
# Rio, outubro de 2022
# --------------------
# ENUNCIADO
# 4. Faça um Programa que peça as quatro notas bimestrais e mostre a média final.
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))
nota4 = float(input('Informe a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Média: {media:02.2f}')