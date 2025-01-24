import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
vitesseInitiale = float(input("Vitesse initiale (en m/s):"))

# Demander l'angle de lancement
angleLancement = float(input("Angle de lancer (en degrés):"))

# Convertir l'angle en radians
angleRadians = angleLancement * (math.pi / 180)

# Calculer la distance maximale en x
distanceMax = (vitesseInitiale ** 2) * math.sin(2 * angleRadians) / g

# Afficher la distance maximale arrondie à 2 chiffres après la virgule
print("Distance parcourue: " + '{:.2f}'.format((round(distanceMax, 2))) + 'm')

# Exemple :
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m
