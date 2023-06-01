import copy


# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


novos_produtos = [
    {**novo_preco, 'preco': round(novo_preco['preco'] * 1.1, 2)}
    for novo_preco in copy.deepcopy(produtos)
]

print('Produtos')
print(*produtos, sep='\n')
print()
print('Novos Produtos')
print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda novo_preco: novo_preco['nome'],
    reverse=True
)

print('Produtos')
print(*produtos, sep='\n')
print()
print('Novos Produtos')
print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda novo_preco: novo_preco['preco']

)

print('Produtos')
print(*produtos, sep='\n')
print()
print('Novos Produtos')
print(*produtos_ordenados_por_preco, sep='\n')



