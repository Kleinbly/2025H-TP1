# Demander le nom complet de l'utilisateur
nom = input("Veuillez entrer votre nom complet : ")

# Demander l'âge de l'utilisateur
age = int(input("Veuillez entrer votre âge : "))

# Définir l'année actuelle
anneeActuelle = 2025

# Calculer l'année de naissance
anneeNaissance = anneeActuelle - age

# Afficher un message de bienvenue avec le nom complet
print("Bonjour " + nom)
# Afficher l'année de naissance
if(anneeNaissance <= anneeActuelle):
    print("Vous êtes né(e) en " + str(anneeNaissance))
