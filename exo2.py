# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
charge = int(input("Entrez le niveau de charge actuel de la batterie : "))

# Vérifiez si le niveau de charge est valide
if charge < 0 or charge > 100:
    print("Erreur : niveau de charge invalide.")
else:
    # Arrondir le pourcentage à la dizaine la plus proche
    charge_arrondie = round(charge / 10) * 10
    # Calculer le nombre de barres
    barres = "❚" * (charge_arrondie // 10)
    espaces = " " * (10 - len(barres))

    # Afficher la représentation graphique de la charge de la batterie
    print(f"[{barres}{espaces}]")
    print(f"{charge}%")

# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%
