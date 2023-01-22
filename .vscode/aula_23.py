nome = str(input('Digite seu primeiro nome: ')).capitalize()
sobrenome = str(input(f'{nome} digite seu sobrenome: ')).capitalize()
ano_nasc = int(input(f'{nome} digite o ano do seu nascimento [XXXX]: '))
idade = 2022 - ano_nasc
altura = float(input(f'{nome} digite sua altura [em metros. ex: 1.60]: '))
maior_idade = idade >= 18

print(f'Seu nome é {nome}, seu sobrenome é {sobrenome}. {nome} você nasceu no ano de {ano_nasc}.\n{nome} você tem {idade} anos, por isso é maior de idade? {maior_idade}. {nome} sua altura é {altura}m.')

