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
