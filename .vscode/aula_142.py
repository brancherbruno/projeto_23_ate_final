# isintstance - para saber se objeto é de determinado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Bruno'}]

for item in lista:
    print(item, isinstance(item, set))

print()
print('*'*20)
print()

for item in lista:
    if isinstance(item, set):
        print(item, isinstance(item, set))

print()
print('*'*20)
print()

for item in lista:
    if isinstance(item, str):
        item.upper()
        print(item, isinstance(item, set))
        print(item.upper())

print()
print('*'*20)
print()


for item in lista:
    if isinstance(item, (int, float)):
        print(item, item *2)

print()
print('*'*20)
print()


