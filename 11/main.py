#!/usr/bin/env python3
from random import shuffle, randint

### Cria as listas já embaralhadas
A = list(range(10))
B = list(range(10))

### Embaralha as listas
shuffle(A)
shuffle(B)

dezenas = []
count = 0 # Contador para lançar 5 dezenas
while(True):
    x = randint(0,9)
    y = randint(0,9)
    if x==y==0:
        continue
    elif count == 5:
        break
    else:
        dezenas.append(int(str(A[x]) + str(B[y])))
        count = count + 1
### Exibe as dezenas sorteadas
print(dezenas)

