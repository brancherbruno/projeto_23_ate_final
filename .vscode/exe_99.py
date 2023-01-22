"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
nome = str(input("Digite seu nome: ")).capitalize()
sair = ""
while True:
    cpf_org = input(f"Digite seu CPF {nome}: ").replace(".", "").replace("-", "").replace(" ", "")
    entrada_sequ = cpf_org == cpf_org[0] * len(cpf_org)
    if entrada_sequ:
        print(f"{nome} você digitou um valor sequencial. Por favor tente novamente.")
        continue

    cpf_9 = cpf_org[:9]
    cpf_10 = cpf_org[:10]
    contador_1 = 10
    resultado_1 = 0
    contador_2 = 11
    resultado_2 = 0

    for nun0 in cpf_9:
        resultado_1 += (int(nun0) * contador_1)
        contador_1 -= 1
    nun1 = resultado_1 * 10
    nun1 = nun1 % 11
    if nun1 <= 9:
        nun1 = nun1
    else:
        nun1 = 0

    for nun3 in cpf_10:
        resultado_2 += int(nun3) * contador_2
        contador_2 -= 1
    nun2 = resultado_2 * 10
    nun2 = nun2 % 11
    if nun2 <= 9:
        nun2 = nun2
    else:
        nun2 = 0

    cpf_gerado = f"{cpf_9}{nun1}{nun2}"

    if cpf_gerado == cpf_org:
        print(f"O cpf {cpf_gerado} é válido.")
    else:
        print(f"O cpf digitado não é válido.")
    sair = str(input(f"{nome} gostaria de sair?")).upper()
    if sair == "S":
        print(f"{nome} obrigado e até logo.")
        break
    elif sair == "N":
        continue
    else:
        print(f"{nome} você precisa digitar [S] para sair ou [N] para continuar")
        
