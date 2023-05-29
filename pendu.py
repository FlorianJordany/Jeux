from math import floor
from random import random


mots = ["python", "programme", "ordinateur", "algorithme", "langage", "variable", "boucle", "fonction", "objet", "condition"]

random = floor(random()*10)

choice=mots[random]

liste=list()

for i in range(len(choice)):
    liste.append("_")

count = 0

while True:
    print("Entrez une lettre ou '?' pour abandonner : ")
    lettre = input()
    if lettre == "?":
        break

    for i in range(len(choice)):
        if lettre == choice[i]:
            liste[i] = lettre

    count += 1

    if "".join(liste) == choice:
        print("Bravo ! Le mot ", choice, " a été trouvé en ", count, " coups")
        break

    print("".join(liste))



