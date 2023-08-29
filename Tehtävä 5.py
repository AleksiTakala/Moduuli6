import random
def parittomat(list):
    for num in list:
        if num % 2 != 1:
            print(num, end=" ")

list1 = []
for i in range(10):
    listaan = random.randint(1,100)
    list1.append(listaan)

print(list1)
paritonlista = parittomat(list1)
print(paritonlista)