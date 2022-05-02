# c = 1
# while c < 10:
#     print(c)
#     c+=1
# print('fim')

# c = 1
# while c != 0:
#     c = int(input('digite um valor: '))
# print('fim')


# sexo = str(input('digite M ou F: ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('dados invalidos ! digite M ou F: ')).strip().upper()[0]
# print('vc digitou {}'.format(sexo))

from faulthandler import cancel_dump_traceback_later
import random
from tkinter import E

# cont = 0
# rand = random.randint(1,10)
# num = 0
# while num != rand:
#     num = int(input('digite um numero: '))
#     cont += 1
# print('o pc pensou em {} e vc tentou {} vezes'.format(rand,cont))

# v1 = 0
# v2 = 0
# v1 = int(input('digite o primeiro valor: '))
# v2 = int(input('digite o segundo valor: '))
# opcao = int(input('''digite [1] para somar:
# digite [2] para multiplicar:
# digite [3] para maior:
# digite [4] para novos numeros:
# ou digite [5] para sair: '''))
# while opcao != 5:    
#     if opcao == 4:
#         v1 = int(input('digite o primeiro valor: '))
#         v2 = int(input('digite o segundo valor: '))
#         opcao = int(input('''digite [1] para somar:
# digite [2] para multiplicar:
# digite [3] para maior:
# digite [4] para novos numeros:
# ou digite [5] para sair: '''))
#     elif opcao == 2:
#         print(f'a multiplicação de {v1} X {v2} = {v1*v2}')
#         break
#     elif opcao == 3:
#         if v1 < v2:
#             print('o maior numero é o {}'.format(v2))
#             break
#         else:
#             print('o maior numero é o {}'.format(v1))
#             opcao = 5
#     elif opcao == 1:
#         print(f'a soma de {v1} + {v2} = {v1+v2} ')
#         break

# valor = int(input('que valor vc quer sacar: R$'))
# total = valor
# cedula = 100
# totalCedula = 0
# while True:
#     if total >= cedula:
#         total -= cedula
#         totalCedula +=1
#     else:
#         if totalCedula > 0:
#             print(f'total de {totalCedula} cedulas de R${cedula}')
#             if cedula == 100:
#                 cedula = 50
#             elif cedula == 50:
#                 cedula = 20
#             elif cedula == 20:
#                 cedula = 10
#             elif cedula == 10:
#                 cedula = 1
#             totalCedula = 0
#             if total == 0:
#                 break