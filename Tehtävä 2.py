import random

Luku = int(input('Anna nopan tahkojen määrä '))

def nopheit():
    noppa = random.randint(1,Luku)
    return noppa
nopheit()
while True:
    luku = nopheit()
    print(luku)
    if luku == Luku:
        break