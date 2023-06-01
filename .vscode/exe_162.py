# Exercício - Adiando execução de funções
# aula sobre func, closeurs
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def nova_funcao(y):
        return funcao(x, y)
    return nova_funcao


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(7))
print()
print(multiplica_por_dez(3))


