# de la part de KORRI: Vous compte est public

print ("Bienvenue au restaurant Pyfood\n") 

print("Les entrées:")
print("1- Salade du chef             12 euos")
print("2- Salade niçoise             10 euros")
print("3- Salade grecque             9  euros")
print("4- Salade italienne           11 euros\n")

choix1 = int(input("Choisissez votre entrée:\n"))
if choix1 == 1:
    print("Vous avez choisi la salade du chef.")
    prix_entrée = 12
elif choix1 == 2:
    print("Vous avez choisi la salade niçoise.")
    prix_entrée = 10
elif choix1 == 3:
    print("Vous avez choisi la salade grecque.")
    prix_entrée = 9
elif choix1 == 4:
    print("Vous avez choisi la salade italienne.\n")
    prix_entrée = 11

print("Les plats:")
print("1- Friture de poissons             25 euros")
print("2- Bavette de veau                 19 euros")
print("3- Saumon à la plancha             22 euros")
print("4- Boeuf bourguignon               16 euros\n")

choix2 = int(input("Choisissez votre plat:\n"))
if choix2 == 1:
    print("Vous avez choisi une Friture de poisson.")
    prix_plat = 25
elif choix2 == 2:
    print("Vous avez choisi une Bavette de veau.")
    prix_plat = 19
elif choix2 == 3:
    print("Vous avez choisi un Saumon à la plancha.")
    prix_plat = 22
elif choix2 == 4:
    print("Vous avez choisi un Boeuf bourguignon.\n")
    prix_plat = 16

print("Les desserts:")
print("1- Crème brûlée             7 euros")
print("2- Tiramissu                8 euros")
print("3- Glace aux choix          9 euros")
print("4- Panacota                 6 euros\n")

choix3 = int(input("Choisissez votre dessert:\n"))
if choix3 == 1:
    print("Vous avez choisi une Crème brûlée.")
    prix_dessert = 7
elif choix3 == 2:
    print("Vous avez choisi un Tiramissu.")
    prix_dessert = 8
elif choix3 == 3:
    print ("Vous avez choisi une Glace aux choix.")
    prix_dessert = 9
elif choix3 == 4:
    print("Vous avez choisi une Panacota.\n")
    prix_dessert = 6

Total = prix_entrée + prix_plat + prix_dessert
print("Le total à payer est {} euros. ".format(Total))











