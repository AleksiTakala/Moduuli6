import random

def nopheit():
    luku = random.randint(1,6)
    return luku
while True:
    luku = nopheit()
    print(luku)
    if luku == 6:
        break