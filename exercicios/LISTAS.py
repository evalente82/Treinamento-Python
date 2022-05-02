# num = [2,5,9,1]
# num[2] = 3 # 
# num.append(7) #insere no inicioa da lista
# num.sort(reverse=True)# ordena de tras p frente
# num.insert(2,0) #insere na posicao 2 o numero 0
# print(num)
# num.pop() #elimina o ultimo, ou eu passo o indice que eu quero remover
# print(num)
# num.remove(0)
# if 9 in num:
#     num.remove(9)
# else:
#     print('nao achei o 9 na lista')
# print(f'essa lista tem {num} elementos')

# valores = []
# valores.append(5)
# valores.append(6)
# valores.append(1)
# valores.append(9)
# for cont in range(0,5):
#     valores.append(int(input('digite valores:')))
# for v in valores:
#     print(f'{v}... ', end='\n')

# for c, v in enumerate(valores):
#     print(f'na posicao {c} encontrei os valores {v}')

# a = [2,3,4,8]
# b = a[:]# para copiar sem fazer uma ligação entre as listas
# b[2] = 9
# print(f'Lista de A: {a}')
# print(f'Lista de B: {b}')

# pessoas = [['pedro',25],['ana', 33],['joao', 50]]

# print(pessoas[0][0])
# print(pessoas[1][1])
# print(pessoas[2][0])
# print(pessoas[1])

# pessoas = [['pedro',25],['ana', 33],['joao', 50],['endrigo',40]]
# for p in pessoas:
#     # print(p) #lista completa
#     # print(p[0]) #só o indice 0 ex só os nomes 
#     # print(p[1]) # só o indice 1 ex só a idade
#     print(f'{p[0]} tem {p[1]} anos')

# galera = list()
# dado = list()
# totmai = totmenor = 0
# for c in range(0,3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# print(galera)

# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade')
#         totmai += 1
#     else:
#         print(f'{p[0]} é MENOR de idade')
#         totmenor += 1
# print(f'temos {totmai} maiores de idade e {totmenor} menores de idade')


# temp = []
# pessoas = []
# maior = menor = 0
# while True:
#     temp.append(str(input('Digite o nome: ')))
#     temp.append(float(input('Digite o peso: ')))
#     if len(pessoas) == 0:
#         maior = menor = temp[1]
#     else:
#         if temp[1] > maior:
#             maior = temp[1]
#         if temp[1] < menor:
#             menor = temp[1]
#     pessoas.append(temp[:])
#     temp.clear()
#     resp = str(input('quer continuar ? [S/N]'))
#     if resp in 'Nn':
#         break
# # print(f'os dados foram {pessoas}')
# print(f'ao todo tem {len(pessoas)}')#tamanho do vetor
# print(f'O maior pesso é {maior}', end='')
# for p in pessoas:
#     if p[1] == maior:
#         print(f'[{p[0]}] ', end= '')
# print()
# print(f'O MENOR pesso é {menor}', end='')
# for p in pessoas:
#     if p[1] == menor:
#         print(f'[{p[0]}] ', end= '')
# print()

# lista = [[],[]]
# valor = 0
# for v in range(1,8):
#     valor = int(input('digite numeros: '))
#     if valor % 2 == 0:
#         lista[0].append(valor)
#     else:
#         lista[1].append(valor)
# lista[0].sort()
# lista[1].sort()
# print(f'os valores pares são: {lista[0]}')
# print(f'os valores ímpares são: {lista[1]}')
# print(lista)

matriz = [[0,0,0,],[0,0,0,],[0,0,0]]
sPar = mai = sCol = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'digite um valor para [{linha}][{coluna}]: '))


for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            sPar += matriz[l][c]
    print()
print(f'a soma dos PARES é : {sPar}')

for l in range(0,3):#
    sCol += matriz[l][2]
print(f'a soma da terceira coluna é {sCol}')

for c in range(0,3):
    if c == 0 :
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'o maior valor da segunda linha é {mai}')