# Curso de Python

## Lista de exercícios 01

### Exercícios – Nível Iniciante
1. Faça um programa que mostre a mensagem "Alô, mundo!" na tela.
2. Faça um programa que peça um nome e mostre uma saudação tipo “Oi,<nome>!” na tela.
3. Faça um programa que peça um número e então mostre a mensagem:
- “O número informado foi [número]”.
A função input usa o formato "string” e aqui devemos fazer uma conversão para inteiro com num =
int(input(“Informe um número: “)).
4. Faça um Programa que peça dois números inteiros e imprima a soma destes.
5. Faça um Programa que peça as quatro notas bimestrais e mostre a média final.
6. Faça um Programa que peça o raio de um círculo, em centímetros, calcule e mostre sua área em centímetros quadrados.
- Dado: PI = 3.14 e A = PI * raio²
7. Faça um Programa que peça o valor do lado de um quadrado e mostre a área e em seguida mostre o dobro desta área para o usuário.
- Dado: area = lado²
8. Faça um programa que peça um número natural e mostre a tabuada de multiplicar(1 a 10) desse número.
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
- Dado: C = 5 * ((F-32) / 9)
10. Faça um Programa que peça dois números e imprima a soma, a subtração, a multiplicação e a divisão entre os números.
11. Faça um programa que receba um número n e imprima na tela os primeiros ‘n’ números quadrados.
12. Faça um programa que peça um número n e informe se esse número é par ou ímpar.
13. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
 
| Média de Aproveitamento | Conceito |
| ------------------- | ------------------- |
| Entre 9.0 e 10.0  | A |
| Entre 7.5 e 9.0 |B |
| Entre 6.0 e 7.5 | C |
| Entre 4.0 e 6.0 | D |
| Entre 4.0 e zero |E |

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO”
se o conceito for A, B ou C ou
“REPROVADO”
se o conceito for D ou E.
14. Faça um programa que receba dois números inteiros e um código de uma
operação (somar, subtrair, multiplicar e dividir) e a execute mostrando o
resultado na tela.

15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem
um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Lembre-se:
Três lados formam um triângulo quando:
A soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
16. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
17. Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e
voltando a pedir as informações.
18. Faça um programa que leia e valide as seguintes informações:
Obs.: Use a função len(string) para saber o tamanho de um texto (o número de
caracteres).
Nome: maior que 3 caracteres;
Idade: entre 1 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
19. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do
outro.
20. Modifique o programa anterior para que ele mostre os números um ao lado do
outro.
21. Faça um programa que leia 5 números e informe o maior número.
22. Faça um programa que leia 5 números e informe a soma e a média dos
números.
23. Faça um programa que imprima na tela apenas os números ímpares entre 1 e
50.
24. Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.
25. Faça um programa que peça dois números, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Não utilize a função de potência
da linguagem.
26. Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números ímpares.
27. A série de Fibonacci é formada pela seguinte sequência: 0,1,1,2,3,5,8,13,21,34,55,
… Faça um programa capaz de gerar a série até o n−ésimo termo informado.
28. A série de Fibonacci é formada pela seguinte sequência:
0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que um número inteiro recebido(o maior não deve ser impresso).
29. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5! = 5.4.3.2.1=120
30. Faça um programa que, dado um conjunto de N números, determine o menor
valor, o maior valor e a soma dos valores.
31. Faça um programa que, dado o nome de um arquivo de texto (loremipsum.txt,
fornecido como exemplo), apresente a quantidade de letras, quantidade de vogais e quantidade de consoantes contidas no mesmo.
32. Faça um programa que leia um arquivo fornecido contendo um conjunto de dados de senhas (codifica.txt fornecido) no formato CODIGO->PALAVRA onde o usuário informe um código e o programa retorne a palavra equivalente.
CODIGO é composto por cinco algarismos numéricos podendo ter algarismo de 1 a 6 em cada
posição. Isso deve ser validado na entrada
Exemplos

 
|Entrada|Saída|
|---|---|
|**Entrada:** 11111  | **Saída:** abacus | 
|**Entrada:** 66666  | **Saída:** zoom  |
|**Entrada:** 88999  | **Saída:** ERRO! Código inexistente  |
|**Entrada:** 111110 | **Saída:** ERRO! Código  inexistente  | 
|**Entrada:** 123456 | **Saída:** ERRO! Código inexistente  |

33. Faça um programa que leia um arquivo contendo o nome e o preço de
diversos produtos(separados por linha), e calcule o total da compra.
34. Implemente um controle simples de mercadorias em uma despensa
doméstica. Para cada produto armazene um código numérico,
descrição e quantidade atual. O programa deve ter opções para
entrada e retirada de produtos, bem como um relatório geral e um
contendo apenas os produtos não disponíveis.

## Desafios – Nível Iniciante
1. Faça um programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidade de latas de tinta a serem compradas e o preço total.
2. Faça um Programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem
compradas e calcule os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misture as latas e os galões, de forma que o desperdício de tinta seja menor.
acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
3. Crie um jogo da velha versão texto para dois jogadores.
4. Crie um jogo de dados versão texto para dois jogadores.
5. Numa eleição existem três candidatos. Faça um programa que peça o número
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de
votos de cada candidato.
6. Crie um jogo de adivinhação de um número inteiro entre num_inferior e
num_superior gerado aleatoriamente que atenda as seguintes especificações:
O usuário escolhe um nível entre três disponíveis:
nível
num_inferior
num_superior
tentativas
novato
mestre
guru
1
1
1
50
70
100
8
5
5
O sistema gera um número inteiro entre inferior e superior para ser adivinhado.
A cada chute, o sistema informa se a chave é maior ou menor que o valor tentado e informa a
quantidade de tentativas realizadas e restantes.
Caso acerte, a mensagem ‘você ganhou’ é exibida e o jogo é finalizado.
Melhore o script para ter a possibilidade de jogar novamente até que o jogador escolha a opção de
sair do jogo.
* Indicamos fortemente o uso do github ou gitlab para que você venha a disponibilizar as suas
respostas destes exercícios propostos na internet.
pythonisk [at] gmail [dot] com
4/4
