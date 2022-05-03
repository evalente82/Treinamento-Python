# DICIONARIO É IGUAL UM OBJETO
# filmes = {
#     'Tilulo': 'Star War',
#     'ano': 1977,
#     'diretor': 'George Lucas'
# }

# print(filmes)
# print(filmes.values())
# print(filmes.keys())
# print(filmes.items())
# for k,v in filmes.items():
#     print(f'O {k} é {v}')


# aluno = {}
# copyLista = []
# for c in range(0,2):
#     aluno['Nome'] = str(input('digite seu nome: '))
#     aluno['Media'] = float(input('digite a media: '))
#     copyLista.append(aluno.copy())

# for e in copyLista:# for para percorrer a lista
#     for k, v in e.items():# items exibe a chave e valor passando por dentro de outro for com 2 indices
#         print(f'O campo {k} tem valor {v}')
#     #print(e)

# for e in copyLista:# for para percorrer a lista
#     for v in e.values():# exibe so os valores
#         print(v)

# print(copyLista)


# aluno = {}
# aluno['nome'] = str(input('Nome: '))
# aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
# if aluno['media'] >= 7:
#     aluno['situacao'] = 'Aprovado'
# elif 5 <= aluno['media'] < 7:
#     aluno['situacao'] = 'Recuperacao'
# else:
#     aluno['situacao'] = 'Reprovado'
# print('-=' *30)
# for k, v in aluno.items():
#     print(f'{k} é igual a {v}')

from random import randint
from time import sleep
from operator import itemgetter
from xml.sax.saxutils import prepare_input_source

# jogo = {
#     'jogador1': randint(1,6),
#     'jogador2': randint(1,6),
#     'jogador3': randint(1,6),
#     'jogador4': randint(1,6),
# }
# rank = list()
# print('VALORES SORTEADOS: ')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)
# rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('-='*30)
# print('Rank dos jogadores: ')
# for i, v in enumerate(rank):
#     print(f'{i+1}º lugar: {v[0]} com {v[1]}')
#     sleep(1)

# from datetime import datetime
# dados = {}
# dados['nome'] = str(input('Digite seu nome: '))
# nasc = int(input('Digite o ano do seu nascimento: '))
# dados['idade'] = datetime.now().year - nasc
# dados['CTPS'] = int(input('Digite o numero da CTPS ou 0 se nao tiver: '))
# if dados['CTPS'] != 0:
#     dados['anoContratacao'] = int(input('Digite o ano da contratação: '))
#     dados['salario'] = float(input('Digite o salário:R$ '))
#     dados['aposentadoria'] = dados['idade'] + ((dados['anoContratacao'] + 35) - datetime.now().year)

# for k, v in dados.items():
#     print(f' - {k} tem o valor {v}')

# jogador = {}
# partidas = list()
# jogador['nome'] = str(input('Digite o nome do jogador: '))
# tot = int(input(f'quantas partidas o {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#     partidas.append(int(input(f'  quantos gols na partida {c} ? ')))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-=' *30)
# print(jogador)
# for k, v in jogador.items():
#     print(f'O campo{k} tem o valor {v}')
# print('-=' *30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'   => Na partida {i+1}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} de gols.')
galera = list()
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N. ')
    if resp == 'N':
        break
print('-=' *30)
print(f'A) Ao todo temos {len(galera)} PESSOAS CADASTRADAS.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estao acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<ENCERRADO>>>')