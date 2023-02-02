# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]


# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()


# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)


def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y

print(
    executa(
        lambda x, y: x / y,
        38, 2
    )
)

# PARA CÓDIGOS MAIS COMPLEXOS É MELHOR UTILIZAR A FUNÇÃO NORMAL, POIS FICA MAIS LEGÍVEL PARA OUTROS PROGRAMADORES.
# # def cria_multiplicador(multiplicador):
# #     def multiplica(numero):
# #         return numero * multiplicador
# #     return multiplica



# ATENÇÃO: PARA COISAS MUITO COMPLEXAS, NÃO UTILIZAR LAMBDA POIS COMO NO EXEMPLO ABAIXO COMENTADO, FICA DIFÍCIL DE ENTENDER OQUE O CÓDIGO QUER DIZER.
# LAMBDA FICA MELHOR PARA CÓDIGOS SIMPLES DE UMA LINHA. 
# duplica = cria_multiplicador(2)
# duplica = executa(
#     lambda m: lambda n: n * m,
#     2
# )
# print(duplica(2))

print(
    executa(
        lambda x, y: x * y,
        2, 3
    ),
)

# QUANDO FOR TRABALHAR VÁRIOS ARGUMENTOS QUE FOREM RECEBIDOS EM X E Y, POSSO UTILIZAR LAMBDA COM ARGS, COMO NO EXEMPLO ABAIXO
print(
    executa(
        lambda *args: sum(args),
        1, 3, 4, 6, 7
    )
)






