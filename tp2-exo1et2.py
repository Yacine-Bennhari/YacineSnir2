moyenne = int (input("Saisir votre moyenne:"))
if moyenne >=18:
    print ("Excellent")
elif moyenne >=14:
    print ("Très Bien")
elif moyenne >=10:
    print ("Assez Bien")
elif moyenne >=5:
    print ("Insuffisant")
elif moyenne <5:
    print ("Catastrophique")






from random import randint
nombre1= randint (1,100)
nombre2= randint (1,100)

print(f"Premier nombre {nombre1}")
print(f"Deuxième nombre {nombre2}")

somme= int (input("Calculer la somme des deux nombres:"))
if somme == nombre1+nombre2:
    print ("Félicitations vous avez trouvé la bonne réponse")
while somme!= nombre1+nombre2:
    somme= int(input("Réésayer ou quitter:"))


