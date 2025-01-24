secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees, reste = divmod(secondes, 31536000)

# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
semaines, reste = divmod(reste, 604800)

# TODO: Assigner à la variable "jours" le nombre de jours restants
jours, reste = divmod(reste, 86400)

# TODO: Assigner à la variable "heures" le nombre d'heures restantes
heures, reste = divmod(reste, 3600)

# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
minutes, reste = divmod(reste, 60)

# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
secondes = reste

# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
print(annees, semaines, jours, heures, minutes, secondes, sep=" ")
