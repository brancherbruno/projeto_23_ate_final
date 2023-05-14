import sys

# Generator expression, Iterables e Iterators

#iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next__
# os __ antes e depois de uma função são chamados de dunders
# iterator = a única responsabilidade dele é entregar 1 
# valor por vez. É saber qual é o próximo valor.

#iterator = iter(iterable)
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

# Generator é uma função que pausa em algum lugar e volta a executar quando for solicitado novamente pelo dev;

#lista = [n for n in range(10000)]
#generator = (n for n in range(10))
#print(sys.getsizeof(lista))
#print(sys.getsizeof(generator))

def generator(n=0, maximum=10):
    while True:
        yield n
        if n >= maximum:
            return 'Acabou!'
        n += 1


gen = generator(n=0)
for n in gen:
    print(n)


# Yield from
def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2()

for n in g:
    print(n)






