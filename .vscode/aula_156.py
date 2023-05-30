import importlib

import aula_156_m

print(aula_156_m.variavel)

for i in range(10):
    importlib.reload(aula_156_m)
    print(i)

print('Fim')