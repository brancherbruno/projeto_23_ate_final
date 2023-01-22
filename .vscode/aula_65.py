nome = str(input('Digite seu nome: ')).upper()
lt = 0
novo_nome = ' '
while lt < len(nome):
    letra = nome[lt]
    novo_nome += f'*{letra}'
    lt += 1
print(novo_nome)