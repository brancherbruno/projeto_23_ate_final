print()
print(20*'=')
print('BEM VINDO A CALCULADORA SIMPLES')
print(20*'=')
sair = ''
oper = ''
nome = str(input('Digite seu nome: ')).capitalize()
while True:
    n1 = float(input(f'{nome} por favor escolha o primeiro número: '))
    n2 = float(input(f'{nome} escolha agora o segundo número: '))
    print('Agora escolha uma operação: ')
    print(' / para divisão')
    print(' + para adição')
    print(' - para subtração')
    print(' * para multiplicação')
    oper = input('Operador: ')
    if oper == '+':
        soma = n1 + n2
        print(f'{nome} soma de {n1} + {n2} é {soma}.')
    elif oper == '-':
        sub = n1 - n2
        print(f'{nome} a subtração de {n1} - {n2} é {sub}.')
    elif oper == '/':
        div = n1 / n2
        print(f'{nome} a divisão de {n1} / {n2} é {div}.')
    elif oper == '*':
        mult = n1 * n2
        print(f'{nome} a multiplicação de {n1} * {n2} é {mult}.')
    else:
        print(f'{nome} você não digitou uma operação válida!')
    sair = str(input(f'{nome} você gostaria de continuar? [S/N]: ')).upper()
    if sair == 'N' and 'n':
        print(f'Obrigado por usar a calculadora {nome}, até breve!')
        break



