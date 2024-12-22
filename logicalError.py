# Objectif : calculer le carré des nombres dans une liste
nombres = [2, 3, 4]
carres = []

for nombre in nombres:
    carres.append(nombre * 2)  # Mauvaise logique : multiplication par 2 au lieu d'élever au carré

print(carres)
