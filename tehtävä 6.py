import math

def pintahinta(lask, hint):
    lask*0.01
    sade = (lask / 2)
    pintala = math.pi*sade**2
    neliohinta = hint/pintala
    return neliohinta

def edukkaampi(pitsa1, pitsa2):
    if pitsa1 < pitsa2:
        print("Pitsa 1 on parempi vastine rahalle")
    elif pitsa1 > pitsa2:
        print("Pitsa 2 on parempi vastine rahalle")
    else:
        print("Pitsat antavat saman vastineen rahalle")



pitsa = int(input("Anna pitsan 1 halkaisija senttimetreinä "))
hinta = int(input("Anna pitsan 1 hinta "))
i = pintahinta(pitsa, hinta)
pitsa = int(input("Anna pitsan 2 halkaisija senttimetreinä "))
hinta = int(input("Anna pitsan 2 hinta "))
a = pintahinta(pitsa, hinta)
print(edukkaampi(i,a))