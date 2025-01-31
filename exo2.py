# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie

# Vérifiez si le niveau de charge est valide

# Arrondir le pourcentage à la dizaine la plus proche

# Calculer le nombre de barres

# Afficher la représentation graphique de la charge de la batterie

# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%
charge = int(input("Entrez le niveau de charge actuel de la batterie : "))

if charge < 0 or charge > 100:
    print("Erreur : niveau de charge invalide.")
else:
    charge_arrondie = round(charge / 10) * 10  # Arrondi à la dizaine
    barres = "\u258a" * (charge_arrondie // 10)  # "❚" représente chaque 10%
    espaces = " " * (10 - len(barres))
    print(f"[{barres}{espaces}]")
    print(f"{charge}%")