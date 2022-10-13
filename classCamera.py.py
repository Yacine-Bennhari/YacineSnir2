class Camera():
    """ Voici la documentation de la classe Camera
        Ses attributs sont:
        - Tdl (Taille de l'image) en Ko
        - ips(image par seconde)

        Ses methodes sont:
        - afficher
    """
    compteur = 0
    def __init__(self,tdl = 18, ips =25):
        self.tdl = tdl
        self.ips = ips
        # print("création d'un objet")
        Camera.compteur+=1
        print("Le nombre d'objets créé est: ",Camera.compteur)
    # def __str__(self) -> str:
    #     return f"""
    #     ******************str***********************
    #     L'objet de la classe Camera a les attributs suivants: 
    #     La taille de l'image (tdl) est {self.tdl} et 
    #     le nombre d'image par seconde appelé ips {self.ips}
    #     ********************************************"""
    def calcule_duree(self,duree ):
        hdd = (self.tdl*self.ips*1024*1024)/duree
        print(f"La taille est: {hdd:.2f}")


    # def __repr__(self) -> str:
    #     return f"""
    #     *****************repr***********************
    #     L'objet de la classe Camera a les attributs suivants: 
    #     La taille de l'image (tdl) est {self.tdl} et 
    #     le nombre d'image par seconde appelé ips {self.ips}
    #     ********************************************"""

    def __getattr__(self,unit):
        print(f"Alerte, il n'y a pas d'attribut {unit} ici")
        

    def afficher(self):
        print(f"""La taille de l'image (tdl) est {self.tdl} et sa capacite ips {self.ips}""" )

maCamera = Camera()
camera2 = Camera(ips =  30,tdl =15  )
maCamera.afficher()
camera2.afficher()

# print(maCamera)
# print(repr(maCamera))
# print(maCamera.__doc__)
# maCamera.calcule_duree(1200000)

maCamera.yacine

maCamera.afficher()
camera2.afficher()