import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

# Calculer le discriminant et assigner la valeur dans la variable "delta"
delta = b ** 2 - (4 * a * c)

# Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable
# "naPasDeSolution"
naPasDeSolution = delta < 0


def formater_racine(x):
    return f"{x:.1f}"  # Affichage des racines avec 2 décimales


if naPasDeSolution:
    # Ces lignes de code seront executé s'il n'y a aucune racine
    # Afficher sur l'écran "Aucune racine"
    print("Aucune racine")
else:
    # Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans
    # "aUneSeuleSolution"
    aUneSeuleSolution = delta == 0

    if aUneSeuleSolution:
        # Ces lignes de code seront executé s'il n'y a une seule racine
        # Afficher sur l'écran "Une seule racine"
        print("Une seule racine")

        # Assigner a la variable x1 la valeur de la racine
        x1 = -b / (2 * a)
        print(formater_racine(x1))
    else:
        # Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans
        # "aDeuxSolutions"
        aDeuxSolutions = delta > 0

        if aDeuxSolutions:
            # afficher sur l'écran "Deux racines"
            print("Deux racines")
            # calculer la première racine, assigner la a "x1"
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            # calculer la deuxième racine, assigner la a "x2"
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(formater_racine(x1), formater_racine(x2))


