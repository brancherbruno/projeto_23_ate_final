# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
# def nao_aceito_zero(d):
#     if d == 0:
#         raise ZeroDivisionError('Você está tentando dividir por zero')
#     return True


# def deve_ser_int_ou_float(n):
#     tipo_n = type(n)
#     if not isinstance(n, (float, int)):
#         raise TypeError(
#             f'"{n}" deve ser int ou float. '
#             f'"{tipo_n.__name__}" enviado.'
#         )
#     return True


# def divide(n, d):
#     deve_ser_int_ou_float(n)
#     deve_ser_int_ou_float(d)
#     nao_aceito_zero(d)
#     return n / d


# print(divide(8, '0'))

def nao_pode_ser_zero(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError('Você está tentado fazer a conta com zero.')
    return True


def deve_ser_real(a):
    tipo_a = type(a)
    a = float(a)
    if not isinstance(a, (float, int)):
        raise ValueError(
            f'"{a}" deve ser um número real.'
            f'"{tipo_a.__name__}" foi digitado.'
        )
    return True


def deve_ser_real2(b):
    tipo_b = type(b)
    b = float(b)
    if not isinstance(b, (float, int)):
        raise ValueError(
            f'"{b}" deve ser um número real.'
            f'"{tipo_b.__name__}" foi digitado.'
        )
    return True


def divide():
    a = float(input('Digite um valor real: '))
    b = float(input('Digite um segundo valor: '))
    deve_ser_real(a)
    deve_ser_real2(b)
    nao_pode_ser_zero(a, b)

    divisao = a/b
    
    print("O resultado da divisão é:", divisao)

divide()
