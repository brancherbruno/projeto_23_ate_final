from random import randint

nome = str(input("Digite seu nome: ")).capitalize()
sair = ""
while True:
    cpf_9 = ""
    cpf_10 = ""
    cpf_gerado = ""
    for i in range(9):
        cpf_9 += str(randint(0, 9))
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
    cpf_10 = cpf_9 + str(nun1)
    for nun3 in cpf_10:
        resultado_2 += int(nun3) * contador_2
        contador_2 -= 1
    nun2 = resultado_2 * 10
    nun2 = nun2 % 11
    if nun2 <= 9:
        nun2 = nun2
    else:
        nun2 = 0

    cpf_gerado = f"{cpf_10}{nun1}"
    print(cpf_gerado)
    if cpf_gerado == str(cpf_10) + str(nun1):
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
        