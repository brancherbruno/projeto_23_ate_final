# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multi(*args):
    total = 1
    for i in args:
        total *= i
    return total
multiplicacao = multi(2, 5, 50)
print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    valor = numero % 2 == 0
    if valor:
        return f"{numero} é par."
    return f"{numero} é ímpar."
total = par_impar(68)
print(total)







