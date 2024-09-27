from random import randint

class Pv:
    '''
    S'occupe de la vie du personnage, des monstres et des objets.
    '''
    def __init__(self, pt_de_vie):
        self.pv = pt_de_vie
        
    def degats(self, attaque):
        self.pv -= attaque
        return self.pv

class Arme:
    '''
    Défini les armes (grade, points de vie, attaque).
    '''
    def __init__(self, grade):
        grades = {'metal': (50, 80, 10), 'bronze': (100, 90, 15), 'argent': (150, 100, 25),
                  'or': (200, 150, 35), 'diamant': (250, 200, 50)}
        self.pv = Pv(grades[grade][1])
        self.grade = grade
        self.attaque = grades[grade][0]
        self.prix = grades[grade][2]

class Perso:
    '''
    Défini le personnage (points de vie).
    '''
    def __init__(self):
        self.pv = Pv(100)

class Monstre:
    '''
    Défini les monstres (points de vie, attaque, catégorie).
    '''
    def __init__(self, categorie):
        cat = {1: (10, 50), 2: (15, 100), 3: (20, 150), 4: (25, 200), 5: (50, 500)}
        self.pv = Pv(cat[categorie][1])
        self.attaque = cat[categorie][0]

class Bouclier:
    '''
    Défini les points de vie des boucliers.
    '''
    def __init__(self, categorie):
        cat = [50, 70, 90, 100, 150, 200]
        self.pv = Pv(cat[categorie])

def fin():
    print("L'histoire s'arrête là, et ta sœur va périr :-(")
    exit()

def choix_debut():
    print("1. Oui")
    print("2. Non")
    return int(input("Choisi en tapant un numéro: "))

def choix_direction():
    print(f"{name_hero}, ton aventure commence devant la porte de ta maison, où voudrais-tu aller ?")
    print("1. Aller en forêt, explorer les horizons")
    print("2. Aller en ville")
    print("3. Rester à la maison")
    return int(input("Choisi une direction:"))

def ville():
    print("Te voilà désormais en ville devant un magasin et des maisons abandonnées.")
    print("Tu as le choix d'aller acheter des armes et des boucliers dans l'armurerie ou explorer les maisons (1/2).")
    choix = int(input("Ton choix : "))
    while choix not in [1, 2]:
        print("Choix non valide, choisis entre 1 ou 2.")
        choix = int(input("Ton choix : "))
    if choix == 1:
        shop()
    elif choix == 2:
        maisons()

def shop():
    global bourse
    print("Tu es rentré(e) dans l'armurerie.")
    print(f"Tu as actuellement {bourse} sous.")
    print("Tu as le choix entre acheter une arme ou un bouclier (1/2).")
    choix = int(input("Ton choix : "))
    if choix == 1:
        print("Choisis une catégorie d'arme :")
        print("1. Métal (10 sous) 2. Bronze (15 sous) 3. Argent (25 sous) 4. Or (35 sous) 5. Diamant (50 sous)")
        arme = int(input("Ton choix : "))
        armes = {1: 'metal', 2: 'bronze', 3: 'argent', 4: 'or', 5: 'diamant'}
        prix = {1: 10, 2: 15, 3: 25, 4: 35, 5: 50}
        if bourse >= prix[arme]:
            bourse -= prix[arme]
            inventaire.append(Arme(armes[arme]))
            print(f"Tu as acheté une épée en {armes[arme]}.")
        else:
            print("Tu n'as pas assez de sous.")
    elif choix == 2:
        print("Les boucliers ne sont pas encore disponibles.")
        
def maisons():
    print("Tu décides d'explorer les maisons abandonnées.")
    print("Certaines sont en ruines, d'autres semblent avoir été abandonnées précipitamment.")
    choix = int(input("Que veux-tu faire ? 1. Fouiller la première maison 2. Passer à la suivante 3. Revenir en ville: "))
    
    if choix == 1:
        objets_possibles = ["une potion de soin", "une épée rouillée", "un bouclier en bois", "un livre ancien", "rien"]
        objet_trouve = objets_possibles[randint(0, len(objets_possibles) - 1)]
        if objet_trouve != "rien":
            print(f"Tu trouves {objet_trouve} dans la maison.")
            inventaire.append(objet_trouve)
            print(f"{objet_trouve} a été ajouté à ton inventaire.")
        else:
            print("Malheureusement, tu ne trouves rien d'utile dans cette maison.")
        maisons()
    elif choix == 2:
        print("Tu passes à la maison suivante...")
        maisons()
    elif choix == 3:
        print("Tu décides de retourner en ville.")
        ville()
    else:
        print("Choix non valide.")
        maisons()

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

def jeu_termine():
    print("Après une longue aventure, tu trouves enfin les baies magiques pour guérir ta sœur.")
    print("Tu rentres au village et soignes Lucie. Félicitations, tu as accompli ta quête !")
    print("Merci d'avoir participé !")
    exit()

# Début de l'aventure
print("Bienvenue dans un monde parallèle au nôtre!")
print("Tu es un jeune héros et ta sœur Lucie est infectée. Ta quête est de la sauver.")
name_hero = input("Saisis le nom de ton personnage : ")

print(f"{name_hero}, es-tu prêt à sauver ta sœur ?")
bourse = 100
inventaire = []

choix1 = choix_debut()
if choix1 == 1:
    print("L'histoire peut commencer!")
else:
    fin()

choix2 = choix_direction()
if choix2 == 1:
    print(f"Ok, tu pars vers la forêt, accompagné de Julie.")
elif choix2 == 2:
    print(f"Ok, tu pars vers la ville, accompagné de Julie.")
    ville()
else:
    fin()
