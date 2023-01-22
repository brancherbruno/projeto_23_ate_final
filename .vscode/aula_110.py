"""
Retorno de valores das funções (return)
"""
# a função return, faz o python parar o código e realizar o código da função, ou seja, dentro da função, se tiver um código após return, ele não será lido.
# Somente se o return estiver dentro de um if, while, etc...

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))


"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
# print(*numeros)
# o *args vai empacotar os itens em uma tupla
# para desempacotar para poder realizar procedimentos como por exemplo, soma, divissao, etc, devo usar *nome_da_variável - o 
# asterisco vai desempacotar oque o *args empacotou liberando para realizar os procedimentos.

