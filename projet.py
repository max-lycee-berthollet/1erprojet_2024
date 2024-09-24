print("Bienvenue dans un monde parallèle au notre! ")
print("Tu es fils ainé de 16ans, avec des frères et soeurs.
Un jour, en rentant de l'ecole, La lumière du soleil filtre à travers les rideaux déchirés.
toute ta famille c'est fait tuer par ces monstres qui souhaite prendre le controle sur le monde.
Ta petite soeur Lucie est la seule survivante de ta famille par miracle. 
Malheureusement ta soeur c'est fait infecter par un de ces monstres. 
Malgré le désespoir que tu puisses avoir, tu dois trouver un remède qui savère etre de baies magiques pour ta soeur qui ce trouve dans un village lointain,
tout en survivant face aux démons et montres que tu pourrais rencontrer dans cette aventure.
")

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
	
print(" ")
def choix_direction():
	print(name_hero,"ton aventure commence devant la porte de ta maison, où voudrais tu aller?")
	print("1.aller en forêt, explorer les horizons")
	print("2.aller en ville")
	print("3.rester à la amison")
	return int(input("choisi une direction:"))

choix2 = choix_direction()
if choix2==1:
	print("Ok, tu pars route vers la forêt, accompagné de Julie")
elif choix2==2:
	print("Ok, tu pars en route vers la ville, accompagné de Julie")
else:
    fin()
from random import randint
class Pv:
    '''
    s occupe de la vie du personnage, des monstres et des objets
    '''
    def __init__(self, pt_de_vie):
        self.cat = categorie
        self.pv = pt_de_vie 
        
    def degats(self, attaque):
        self.pv -= attaque
        return self.pv
    
class Arme:
    '''
    defini les armes (grade, pt de vie, attaque)
    '''
    def __init__(self, grade):
        grades = {'metal':(50,80),'bronze':(100,90),'argent':(150,100), 'or':(200,150),'diamant':(250,200)}
        self.pv = Pv(grades[grade][1])
        self.grade = grade
        self.attaque = grades[grade][0]
        
    def attaque(self):
        return self.attaque
    
class Perso:
    '''
    defini le personnage (pt de vie,)
    '''
    def __init__(self):
        self.pv = Pv(100)
        
class Monstre:
    '''
    defini les monstres (pt de vie, attaque, categorie)
    '''
    def __init__(self, categorie):
        cat = {1:(10,50), 2:(15,100), 3:(20,150), 4:(25, 200), 5:(50, 500)}
        self.pv = Pv(cat[categorie][1])
        self.attaque = cat[categorie][0]

class Bouclier:
    '''
    defini les pv des boucliers
    '''
    def __init__(self, categorie):
        cat = [50,70,90,100,150,200]
        self.pv = Pv(cat[categorie])
