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


