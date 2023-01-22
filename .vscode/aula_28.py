nome = str(input('Por favor digite seu nome: ')).capitalize()
idade = int(input(f'{nome}, qual sua idade? '))
altura = float(input(f'{nome}, por favor digite sua altura [ex: 1.65] '))
peso = float(input(f'{nome} agora digite seu peso [em kg ex: 75.45] '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'{nome}, você tem {idade} anos, sua altura é {altura}m e seu peso é {peso}kg. Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif 18.5 < imc < 24.9:
    print(f'{nome}, você tem {idade} anos, sua altura é {altura}m e seu peso é {peso}kg. Seu IMC é {imc:.2f} e você está no peso ideal.')
elif 25 < imc < 29.9:
    print(f'{nome}, você tem {idade} anos, sua altura é {altura}m e seu peso é {peso}kg. Seu IMC é {imc:.2f} e você está acima do peso.')
elif 30 < imc < 34.9:
    print(f'{nome}, você tem {idade} anos, sua altura é {altura}m e seu peso é {peso}kg. Seu IMC é {imc:.2f} e você está com obesidade grau 1.')
elif 35 < imc < 39.9:
    print(f'{nome}, você tem {idade} anos, sua altura é {altura}m e seu peso é {peso}kg. Seu IMC é {imc:.2f} e você está com obesidade grau 2.')
else:
    print(f'{nome}, você tem {idade} anos, sua altura é {altura}m e seu peso é {peso}kg. Seu IMC é {imc:.2f} e você está com obesidade grau 3.')





