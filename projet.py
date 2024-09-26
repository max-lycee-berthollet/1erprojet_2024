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

print("Bienvenue dans un monde parallèle au notre! ")
print("Tu es fils ainé de 16ans, avec des frères et soeurs.
Un jour, en rentant de l ecole, La lumière du soleil filtre à travers les rideaux déchirés.
toute ta famille c est fait tuer par ces monstres qui souhaite prendre le controle sur le monde.
Ta petite soeur Lucie est la seule survivante de ta famille par miracle. 
Malheureusement ta soeur c est fait infecter par un de ces monstres. 
Malgré le désespoir que tu puisses avoir, tu dois trouver un remède qui savère etre de baies magiques pour ta soeur qui ce trouve dans un village lointain,
tout en survivant face aux démons et montres que tu pourrais rencontrer dans cette aventure.")

name_hero=str(input("sasir le nom de ton personnage: "))
print(name_hero,", es-tu prêt à sauver ta soeur ?")

bourse = 100
inventaire = []

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
	ville()
else:
    fin()
    
def ville():
    print('Te voila desormais en ville tu te trouves devant un magasin aisni que des maisons abandonnées')
    print('Tu as soit le choix d aller acheter des armes et des boucliers dans l armurerie ou aller explorer les differentes maisons (1/2)')
    choix = int(input('ton choix : '))
    while choix != 1 or choix != 2:
        print('ton choix n est pas valide choisit entre 1 ou 2')
        choix = int(input('ton choix : '))
    if choix == 1:
        shop()
    elif choix == 2:
        maisons()
        
def shop():
    print('Tu es rentré(e) dans l armurerie')
    print(f'Tu as actuellement {bourse} dans ta bourse')
    print('Tu as le choix entre acheter une arme ou un bouclier (1/2)')
    choix = int(input('ton choix : '))
    if choix == 1:
        print('Tu as le choix entre plusieurs catégories d arme')
        print('metal (50 d attaque, 80 pv, 10 sous),bronze (100 d attaque, 90 pv, 15 sous),argent (150 d attaque, 100 pv, 25 sous),or (200 d attaque, 150 pv, 35 sous),diamant (250 d attaque, 200 pv, 50 sous) (1/2/3/4/5)')
        arme = int(input('ton choix : '))
        if arme == 1:
            bourse -= 10
            inventaire.append('epée en metal')





# tu as 4 fonctions en vif tu en fais ce que tu veux mais elles sont la


class Arme:
    def __init__(self, pv, grade, attaque):
        self.pv = pv        # Points de vie de l'arme
        self.grade = grade  # Matériau de l'arme
        self.attaque = attaque  # Puissance d'attaque de l'arme

    def afficher_info(self):
        """Affiche les informations de l'arme."""
        return f"Arme: {self.grade}, PV: {self.pv}, Attaque: {self.attaque}"

    def soustraire_pv(self, valeur):
        """Soustrait une valeur aux points de vie de l'arme."""
        if valeur < 0:
            print("La valeur à soustraire doit être positive.")
        else:
            self.pv -= valeur
            # S'assurer que PV ne tombe pas en dessous de 0
            if self.pv < 0:
                self.pv = 0
            print(f"Points de vie mis à jour : {self.pv}")

# Création de l'objet Couteau en passant les arguments directement
mon_couteau = Arme(pv=100, grade="metal", attaque=50)

# Affichage des informations du couteau
print(mon_couteau.afficher_info())

# Affichage des attributs individuels
print("Attributs du couteau :")
print(f"Points de vie (PV) : {mon_couteau.pv}")
print(f"Grade : {mon_couteau.grade}")
print(f"Attaque : {mon_couteau.attaque}")



def maisons():
    print("Tu décides d'explorer les maisons abandonnées.")
    print("Certaines sont en ruines, d'autres semblent avoir été abandonnées précipitamment.")
    
    choix = int(input("Que veux-tu faire ? 1. Fouiller la première maison 2. Passer à la suivante 3. Revenir en ville: "))
    
    if choix == 1:
        # Génération aléatoire d'objets trouvés
        objets_possibles = ["une potion de soin", "une épée rouillée", "un bouclier en bois", "un livre ancien", "rien"]
        objet_trouve = objets_possibles[randint(0, len(objets_possibles) - 1)]
        
        if objet_trouve != "rien":
            print(f"Tu trouves {objet_trouve} dans la maison.")
            inventaire.append(objet_trouve)
            print(f"{objet_trouve} a été ajouté à ton inventaire.")
        else:
            print("Malheureusement, tu ne trouves rien d'utile dans cette maison.")
        
        # Après avoir fouillé la première maison, on peut fouiller d'autres maisons
        maisons()  # Appelle la fonction à nouveau pour continuer l'exploration des maisons
    elif choix == 2:
        print("Tu passes à la maison suivante...")
        maisons()  # Continue l'exploration
    elif choix == 3:
        print("Tu décides de retourner en ville.")
        ville()  # Retourne à la ville
    else:
        print("Choix non valide. Essaie encore.")
        maisons()  # Répète le choix si l'entrée n'est pas valide

     
def combat(monstre, perso, arme):
    print("Un monstre approche!")
    while monstre.pv.pv > 0 and perso.pv.pv > 0:
        action = int(input("Que veux-tu faire ? 1. Attaquer 2. Fuir: "))
        if action == 1:
            print("Tu attaques le monstre !")
            monstre.pv.degats(arme.attaque)
            print(f"Le monstre a {monstre.pv.pv} points de vie restants.")
            if monstre.pv.pv > 0:
                print("Le monstre riposte !")
                perso.pv.degats(monstre.attaque)
                print(f"Tu as {perso.pv.pv} points de vie restants.")
        else:
            print("Tu fuis le combat...")
            break
    if perso.pv.pv <= 0:
        print("Tu es mort ! Game Over.")
        fin()
    elif monstre.pv.pv <= 0:
        print("Tu as vaincu le monstre !")
    
    
    
    def jeu_terminer():
    print("Après une longue aventure, tu trouves enfin les baies magiques pour guérir ta sœur.")
    print("Tu rentres au village et soignes Lucie. Félicitations, tu as accompli ta quête !")
    print("Merci d'avoir participé! ")
    exit()














