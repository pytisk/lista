# # ------------- # #
# Script em python para gerar arquivos no diretório corrente
# Formato do nome do arquivo: exnn.py
# onde nn é um número incrementado a partir de 01
# até a quantidade informada.

import sys
import os

# Pegar a quantidade de arquivos a serem criados
qtd = int(input('Quantidade de arquivos: '))

# Informações  iniciais
pre = 'ex'
pos = '.py'
linha = '# '+'-'*20
texto1 = '# Lista 01\n# Arquivo: parte03/'
texto2 = '# Autor: mweb - pythonisk team\n# Rio, outubro de 2022'
for i in range(qtd):
    filen = f'{pre}{i+1:02}{pos}'
    conteudo = f'{linha}\n{texto1}{filen}\n{texto2}\n{linha}\n'
    with open(filen, 'w') as arquivo:
        arquivo.write(conteudo)
print(f'{qtd} arquivos foram criados com sucesso!')

