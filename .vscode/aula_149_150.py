# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError:
#     print('Dividiu por zero.')
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError):
#     print('TypeError + IndexError')
# except Exception:
#     print('ERRO DESCONHECIDO.')

# print('CONTINUAR')


# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     # print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO.')

# print('CONTINUAR')

try:
    a = int(input('Digite um valor inteiro: '))
    print()
    b = int(input('Digite o valor que você quer dividir: '))

    c = a/b
    print(c)

    
except (TypeError, IndexError, ZeroDivisionError, ValueError) as e:
    print('Nome', e.__class__.__name__)
    print(e)
    print('Error')
print('Fim')


