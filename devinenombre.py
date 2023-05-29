from math import floor
from random import random

ordi = floor(random()*30 + 1)

print("J'ai choici un nombre entre 1 et 30")
print("A vous de le deviner en 5 tentatives maximum !")

count = 0

while count <= 4:
    count += 1
    choice = int(input())

    if ordi == choice:
        print("Bravo ! vous avez trouvé ", ordi, " en ", count , " essais")
        break
    elif choice < ordi:
        print("Trop petit")
    else:
        print("Trop grand")








