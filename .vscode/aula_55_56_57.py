"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

"""

numero = 0
sair = " "

while True:
    numero = input('Digite um numero inteiro [sem virgula e positivo]: ')
    if numero.isdigit():
        num_int = int(numero)
        if (num_int % 2) == 0:
            print(f'O número {numero} é par.')
        else:
            print(f'O número {numero} é ímpar.')
    else:
        print(f'O número {numero} não é inteiro, por favor insira um número inteiro, sem virgula e positivo.')
    sair = str(input('Gostaria de sair? [S/N]: ')).upper()
    if sair == "S" and "s":
        print('Obrigado por testar. Até breve.')
        break
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
hora = 0
sair = " "

while True:
    hora = input('Digite a hora no formato de hora inteira [ex: 15]: ')
    if hora.isdigit():
        hora_int = int(hora)
        if 0 <= hora_int <= 11:
            print('Bom dia!')
        elif 12 <= hora_int <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('Você não digitou um valor de hora correto. Favor repetir.')
    sair = str(input('Gostaria de sair? [S/N]')).upper()
    if sair == "S" and "s":
        print('Obrigado e até a próxima!')
        break
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = " "
sair = ' '
while True:
    nome = input('Digite seu primeiro nome: ').capitalize()
    if len(nome) <= 4:
        print(f'{nome} seu nome é curto.')
    elif 5 <= len(nome) <=6:
        print(f'{nome} seu nome é normal.')
    else:
        print(f'{nome} seu nome é longo.')
    sair = str(input(f'Você gostaria de sair {nome}? [S/N]')).upper()
    if sair == 'S' and 's':
        print(f'{nome} obrigado e até logo.')
        break