# Exercício - sistema de perguntas e respostas


from functools import total_ordering


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

sair = ''
total_acerto = 0
nome = str(input('Qual seu nome? ')).capitalize()
while True:
    for pergunta in perguntas:
        print("Pergunta: ", pergunta['Pergunta'])
        opcoes = pergunta['Opções']
        for i, opcao in enumerate(opcoes):
            print(f"{i})", opcao)
        acertou = False 
        escolha = input(f"{nome} escolha sua resposta: ")
        int_escolha = None
        total_opces = len(opcoes)

        if escolha.isdigit():
            int_escolha = int(escolha)
        if int_escolha is not None:
            if int_escolha <= total_opces and int_escolha >= 0:
                if opcoes[int_escolha] == pergunta['Resposta']:
                        acertou = True
    if acertou:        
            total_acerto += 1
            print()
            print(f"Parabéns {nome}, você acertou!")
            print(20*'=')
            print()
            
    else:
        print()
        print(f"Que pena {nome}, você errou!")
        print(20*'=')
        print()

    print(f'{nome} você acertou {total_acerto} pergunta(s) de', len(perguntas), 'pergunta(s).')  
    print()
    print()
    
    sair = str(input(f'{nome} gostaria de sair?')).upper()
    if sair == 'S':
        print(f'Obrigado {nome}, até breve.')
        break
    elif sair == 'N':
        continue
    else:
        print(f"Você não digitou uma resposta válida, por favor digite S para sair ou N para continuar.")
        sair = str(input(f'{nome} gostaria de sair?')).upper()
