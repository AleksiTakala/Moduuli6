import random

def summa(list):
    su = sum(list)
    return su


list1 = []
for i in range(5):
    listaan = random.randint(0,100)
    list1.append(listaan)

summ = summa(list1)
print(summ)

