print("Bienvenue dans un monde parallèle au notre! ")
print("""Tu es fils ainé de 16ans, avec des frères et soeurs.
Un jour, en rentant de l'ecole, La lumière du soleil filtre à travers les rideaux déchirés.
toute ta famille c'est fait tuer par ces monstres qui souhaite prendre le controle sur le monde.
Ta petite soeur Lucie est la seule survivante de ta famille par miracle. 
Malheureusement ta soeur c'est fait infecter par un de ces monstres. 
Malgré le désespoir que tu puisses avoir, tu dois trouver un remède qui savère etre de baies magiques pour ta soeur qui ce trouve dans un village lointain,
tout en survivant face aux démons et montres que tu pourrais rencontrer dans cette aventure.
""")

name_hero=str(input("sasir le nom de ton personnage: "))
print(name_hero,", es-tu prêt à sauver ta soeur ?")

def fin():
	print("L'histoire s'arrête là, et ta soeur va périr :-(")
	exit()
    """
      fin:
        quand cette fonction est appelé, le programme s'arrete
    """
def choix_debut():
	print("1.Oui")
	print("2.Non")
	return int(input("Choisi en tapant un numéro: "))

    """
      choix_debut:
	on doit choisir l'endroit où nous voulons aller
	return (type): choisir l'endroit avec un numero
    """

choix1=choix_debut()
if choix1==1:
	print("l'histoire peut commencer!")
else:
	fin()
	
print(""" """)
def choix_direction():
	print(name_hero,"ton aventure commence devant la porte de ta maison, où voudrais tu aller?")
	print("1.aller en forêt, explorer les horizons")
	print("2.aller en ville")
	print("3.rester à la amison")
	return int(input("choisi une direction:"))

choix2= choix_direction()
if choix2==1:
	print("Ok, tu pars route vers la forêt, accompagné de Julie")
elif choix2==2:
	print("Ok, tu pars en route vers la ville, accompagné de Julie")
else:
    fin()






class Pv:
    '''
s'occupe de la vie du personnage et des objets
    '''
    def __init__(self, categorie):
        self.cat = categorie
        self.pv = 100
    def degats(self):
        self.pv -= 4
        return self.pv
    
class Arme:
    def __init__(self):
        self.pv = Pv(perso)
    def attaque(self):
        attaque = 0
        return attaque
