import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

delta = b ** 2 - 4 * a * c  # Calcul du discriminant
naPasDeSolution = delta < 0


def formater_racine(x):
    return f"{x:.2f}"  # Affichage des racines avec 2 décimales


if naPasDeSolution:
    print("Aucune racine")
else:
    aUneSeuleSolution = delta == 0

    if aUneSeuleSolution:
        print("Une seule racine")
        x1 = -b / (2 * a)
        print(formater_racine(x1))
    else:
        aDeuxSolutions = delta > 0

        if aDeuxSolutions:
            print("Deux racines")
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(formater_racine(x1), formater_racine(x2))


