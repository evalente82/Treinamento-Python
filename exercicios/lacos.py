
# for c in range(0,6):#percorre normal
#     print(c)
# print('fim')

# for c in range(6,0,-1):#percorre de tras pra frente
#     print(c)
# print('fim')

# for c in range(0,7,2):#percorre pulando de 2 em 2
#     print(c)
# print('fim')

# n = int(input('digite um numero: '))

# for c in range(1,n+1):
#     print(c)
# print('fim')

# i = int(input('digite inicio: '))
# f = int(input('digite o fim: '))
# p = int(input('digite de qtos em qtos: '))

# for c in range(i,f+1,p):
#     print(c)
# print('fim')

# s = 0
# for c in range(0,4):
#     n= int(input('digite um valor: '))
#     s += n
# print('a soma é {}'.format(s))
# from time import sleep

# for cont in range(10, -1, -1):
#     print(cont)
#     sleep(1)
# print('boommm')

# for count in range(1,50+1):
#     if count % 2 == 0:
#         print('o numero : {} é par'.format(count))

# soma = 0
# for count in range(1,500+1):
#     if count % 2 == 1:
#         if count % 3 == 0:
#             soma += count
#             print('o numero : {} é multiplo de 3'.format(count))
# print('a soma dos multiplos de 3 é {}'.format(soma))

# num = int(input('digite um numero pra gerar a tabuada: '))
# for c in range(1,10+1):
#     total = num * c
#     print('{} X {} = {} '.format(num,c, total))


# soma = 0
# for c in range(1,3+1):
#     num = int(input('digite um numero:'))
#     if num % 2 == 0:
#         soma += num

# print('a soma dos pares é: {}'.format(soma))

# num = int(input('digite um numero: '))
# for c in range(1,5+1):
#     print('{} '.format(c), end='')

# n = str(input('digite um nome: ')).strip()
# nome = n.split()
# print('seu primeiro nome é {} e seu ultimo nome é {}'.format(nome[0], nome[len(nome)-1]))

# frase = str(input('digite uma frase para saber se é palindromo: ')).strip().upper()#TIRA OS ESPAÇOS
# palavras = frase.split()#TRANFORMA EM ARRAY DE PALAVRAS
# junto = ''.join(palavras)#JUNTA O QUE ESTA DENTRO DO ARRAY ''
# inverso = ''#CRIA A VAR INVERSO PARA SALVAR E DEPOIS COMPARAR COM A FRASE SEM ESPAÇO
# for letra in range(len(junto) -1, -1, -1):#TAMANHO DE JUNTO DE 19 ATE -1
#     # DE TRAS P FRENTE ATE A ULTIMA LETRA Q É -1 E VOLTA DE UMA EM UMA LETRA -1
#     inverso += junto[letra]#JOGO A FRASE DE TRAS P FRENTE PARA A VAR

# if inverso == junto:
#     print('a frase é um palindromo')
#     print(junto, inverso)
# else:
#     print('a frase NÃO é um palindromo')
#     print(junto, inverso)

from datetime import date
# atual = date.today().year
# totalMaior = 0
# totalMenor = 0
# for pess in range(1,8):
#     nasc = int(input('em que ano a {}ª pessoa nasceu :'.format(pess)))
#     idade = atual - nasc
#     print('essa pessoa tem {} anos.'.format(idade))
#     if idade >= 21:
#         totalMaior += 1
#     else:
#         totalMenor += 1
# print('total de maiores de idade são: {}'.format(totalMaior))
# print('total de MENORES de idade são: {}'.format(totalMenor))

# mediaIdade = 0
# nomeHomemVelho =''
# mulheresMenos20 = 0
# maior = 0
# for pessoa in range(1,5):
#     nome = str(input('digite o nome: [{}]'.format(pessoa)))
#     idade = int(input('digite sua idade:[{}]'.format(pessoa)))
#     sexo = str(input('digite M para maculino e F para feminino:[{}]'.format(pessoa)))
#     mediaIdade = mediaIdade + idade / 4
#     if sexo == 'M':
#         if maior < idade: 
#             maior = idade
#             nomeHomemVelho = str(nome)
#             print(nome)
#     if sexo == 'F':
#         if idade < 20:
#             mulheresMenos20 += 1
# print('a media do grupo é : {}'.format(mediaIdade))
# print('nome do homem mais velhor é: {}'.format(nomeHomemVelho))
# print('total de mulheres com menos de 20 anos: {}'.format(mulheresMenos20))

