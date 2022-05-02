
# preco = float(input('qual o preço do produto: R$')) 

# novo = preco - (preco * 5 / 100)

# print( 'preço preço R${:.2f} com desconto vai para R${:.2f}'.format(preco, novo))
# print('*******************************************************')
# salario = float(input('qual o salario do cara: R$'))

# aumento = salario + (salario * 15 / 100)

# print( 'o salario atual é R${:.2f} com aumento de 15% vai para R${:.2f}'.format(salario, aumento))
# print('*******************************************************')

# c = float(input('digita a temperatura em ºC: '))
# f = ( (9*c) /5) + 32 # ou 9 * c / 5 + 32
# print('a temperatura de {:.2f}ºC corresponde a {:.2f}ºF'.format(c,f)) 
# print('*******************************************************')
# km = float(input('qtd de km rodado: '))
# dias = int(input('qtd de dias que ficou com o carro: '))
# diaAlugado = float(60)
# kmRodado = float(0.15)
# valorKM = km * kmRodado
# valorDia = dias * diaAlugado
# total = valorKM + valorDia
# print('total a pagar R${}'.format(total))
# print('*******************************************************')

# import math
# from math import pow
# num = int(input(' numero: '))
# raiz = math.sqrt(num)
# print('a raiz é {}'.format(math.ceil(raiz)))
# ceil arredonda pra cima
# floor arredonda pra baixo
# trunc
# pow potencia
# sqrt raiz quadrada
# factorial

# print('*******************************************************')


# num = random.random()
# num2 = random.randint(1,10)
# print(num2)
# print('*******************************************************')

import math
import random

# num = int(input('digite um numero: '))

# sucessor = num + 1
# antecessor = num - 1
# print('sucessor {} antecessor {}'.format(sucessor, antecessor))

# num = int(input('digite um numero: '))
# d = num * 2
# t = num * 3
# raiz = math.sqrt(num)
# print('vc digitou {} o dobro é: {} o triplo é: {} e a raiz quadrada é {}'.format(num,d,t,raiz))

# av1 = float(input('digite a nota av1: '))
# av2 = float(input('digite a nota av2: '))
# media = (av1 + av2) / 2
# print('a media é {}'.format(media))
# metros = float(input('digite os metros: '))
# centimetros = metros * 100
# milimetros = metros * 1000
# print('resultado centimetros {:.2f} resultado milimetros {:.2f}'.format(centimetros, milimetros))

# n = str(input('digite um nome: ')).strip()
# nome = n.split()
# print('seu primeiro nome é {} e seu ultimo nome é {}'.format(nome[0], nome[len(nome)-1]))

# tempo = int(input('digite o tempo de uso do carro: '))
# print('carro novo' if tempo <= 3 else 'carro velho')
# print('fim')

# num = random.random()
# num2 = random.randint(1,5)
# adivinhe = int(input('digite um numero para adivinhar o random: '))

# if num2 == adivinhe:
#     print('acertou ! vc digitou {} e o computador pensou {}'.format(adivinhe, num2))
# else:
#     print('Errou ! vc digitou {} e o computador pensou {}'.format(adivinhe, num2))

# num = int(input('digite um numero: '))
# resultado = num % 2#num dividido por 2 guarda o resto em resultado
# #resultado sempre sera 0 para par ou 1 para impar 
# print('par' if resultado == 0 else 'impar')

# distancia = float(input('qual a distancia em km: '))

# km = float(0.50)
# km2 = float(0.45)
# a = km * distancia
# b = km2 * distancia

# if distancia > 200:
#     print('o valor é: R${:.2f}'.format(b))
# else:
#     print('o valor é: R${:.2f}'.format(a))

# salario = float(input('digite seu salario: '))

# if salario > 1250.00:
#     total = salario * 10 /100
#     total2 = total + salario
#     print('seusalario aumentará em R${} dando um total de R${}'.format(total, total2))
# else:
#     total = salario * 15 / 100
#     total2 = total + salario
#     print('seusalario aumentará em R${} dando um total de R${}'.format(total, total2))

# print('-='*20)
# print('analisador de triangulos')
# print('-='*20)

# r1 = float(input('primeiro segmento: '))
# r2 = float(input('segundo segmento: '))
# r3 = float(input('terceiro segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
#     print('forma trinagulo')
# else:
#     print('não forma trinagulo')

# vCasa = float(input('digite o valor da casa: '))
# vSalario = float(input('digite o valor do seu salário: '))
# vAno = float(input('digite em quatos anos vc vai pagar: '))

# messes = int(vAno * 12)
# prestacao = float(vCasa / messes)

# v30 = (vSalario * 30) / 100

# if v30 >= prestacao:
#     print(
#         'Autorzado ! 30% do seu salario é R${:.2f} sua prestação fica em R${:.2f} total de messes á pagar {}'
#     .format(v30, prestacao, messes))
# else:
#     print(
#         'Negado ! 30% do seu salario é R${:.2f} sua prestação fica em R${:.2f} total de messes á pagar {}'
#     .format(v30, prestacao, messes))

# num = int(input('digite um numero inteiro: '))
# print(''' escolha uma das bases para converão:
# [1] binario
# [2] octal
# [3] hexadecimal
# ''')
# opcao = int(input('vc escolheu: '))
# if opcao == 1:
#     print('{} Convertido para binario é igual a {}'.format(num, bin(num)))
# elif opcao == 2 :
#     print('{} Convertido para octal é igual a {}'.format(num, oct(num)))
# elif opcao == 3:
#     print('{} Convertido para hexadecimal é igual a {}'.format(num, hex(num)))
# else:
#     print('opcao invalida !')

