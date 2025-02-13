import time
import random
from utils import espace
from potion import PotionNiveau1,PotionNiveau2

class Personnage:
    def __init__(self, nom, niveau = 1, pdv = 50, force = 5, vitesse=10,experience=0):
        self.nom = nom
        self.niveau = niveau
        self.pdvMax = pdv
        self.pdv = pdv
        self.force = force
        self.vitesse = vitesse
        self.niveau_max = 30
        self.experience = experience
        self.inventaireSoins = {
            PotionNiveau1:0,
            PotionNiveau2:0
            }
                           
    #Permet d'afficher les infos du perso   
    def afficher_informations(self):
        espace(1)
        time.sleep(1)
        print(f"Nom : {self.nom}")
        print(f"Niveau : {self.niveau} / {self.niveau_max}")
        print(f"Points de vie : {self.pdv}/{self.pdvMax}")
        print(f"Force : {self.force}")
        print(f"Precision : {self.precision} / {self.precision_max}")
        print(f"Vitesse : {self.vitesse}")
        self.afficher_experience_sur_experience_necessaire()
        espace(1)

    # Permet d'afficher sa santé/santé max
    def afficher_sante(self):
        espace(1)
        time.sleep(1)
        print(f"Santé de : {self.nom} est de {self.pdv}/{self.pdvMax}")
        espace(1)

    # methode attaquer
    def attaquer(self, cible):
        espace(1)
        time.sleep(1)
        if self.pdv > 0:
                
                if cible.pdv > 0:
                    cible.recevoir_degats(self.force)
                    if(cible.pdv == 0):

                        print(f"{self.nom} à gagné ! {cible.nom} est mort !")
                        espace(1)
        else:
            print(f"{self.nom} ne peut pas attaquer {cible.nom} car {cible.nom} est mort.")

    # methode recevoir degat
    def recevoir_degats(self, degats):
        espace(1)
        time.sleep(1)
        self.pdv -= degats
        if self.pdv > 0:
            print(f"{self.nom} a reçu {degats} pts de dégats.")
            self.afficher_sante()
        else:
            self.pdv = 0

    def afficher_experience_sur_experience_necessaire(self):
        print(f"Experience : {self.experience}/{self.experience_necessaire_niveau_suivant()}")

    # methode qui permet de gagner de l'experience
    def gagner_experience(self,experience):
        self.experience += experience
        self.gain_niveau()

    # methode experience necessaire passage de niveau 
    def experience_necessaire_niveau_suivant(self):
        experience_necessaire_niveau_suivant = self.niveau * 100
        return experience_necessaire_niveau_suivant

    # methode de gain de niveau
    def gain_niveau(self):

        if self.niveau <= self.niveau_max:
            while self.experience >= self.experience_necessaire_niveau_suivant():
                self.experience -= self.experience_necessaire_niveau_suivant()  # On soustrait l'expérience nécessaire pour passer au niveau suivant
                self.niveau += 1
                self.pdv = int(self.pdv*1.2)
                self.pdvMax = int(self.pdvMax*1.2)
                self.force = int(self.pdv*1.2)
                print(f"Félicitations ! Vous venez de passer au niveau : {self.niveau}")
                self.afficher_difference_caracteristique_gain_niveau()
                self.afficher_informations()
        else:
            print("niveau max déjà atteint !")

    # Permet d'afficher l'inventaire de soins du perso
    def afficher_inventaire_potion(self):
        espace(1)
        time.sleep(1)
        print("Inventaire : ")
        for i in self.inventaireSoins:
            time.sleep(1)
            print(f"{i.libelle} x {self.inventaireSoins[i]}")
        espace(1)

    # Permet de choisir dans l'inventaire du perso
    def choisir_dans_inventaire_potion(self):
        libelle_to_objet = {objet.libelle: objet for objet in self.inventaireSoins.keys()}
        # Crée un dictionnaire temporaire pour associer chaque libellé d'objet à son objet correspondant.
        # Utile pour retrouver un objet à partir du choix utilisateur plus bas (libellé).

        choixUserInventaire=""

        while choixUserInventaire !="q":
            espace(1)
            time.sleep(1)
            print("Veuillez choisir une Potion ou taper 'q' pour quitter")
            espace(1)
            time.sleep(1)
            self.afficher_inventaire_potion()

            choixUserInventaire = str(input("Pour choisir une potion veuillez réecrire son libelle : "))
            if choixUserInventaire in libelle_to_objet:
                objet = libelle_to_objet.get(choixUserInventaire)
                # Vu que libelle present on récupère l'objet du mapping fais plus haut
                if(self.inventaireSoins[objet]>0):
                    self.utliser_objet_soin(objet)
                    self.afficher_inventaire_potion()
                    break
                else:
                    espace(1)
                    time.sleep(1)
                    print(f"Action Imposible ! Vous n'avez plus : {objet.libelle} dans votre inventaire")
            elif(choixUserInventaire=="q"):
                espace(1)
                time.sleep(1)
                print("Fermeture de l'inventaire de soin")
            else:
                espace(1)
                time.sleep(1)
                print("Choix Invalide")
                espace(1)

    
    def enlever_objet_soin(self,pObjetSoin):
        espace(1)
        if self.inventaireSoins[pObjetSoin]>0 :
            self.inventaireSoins[pObjetSoin]-= 1
            print(f"Il ne vous reste plus que : {self.inventaireSoins[pObjetSoin]} {pObjetSoin.libelle}")
        espace(1)

    def utliser_objet_soin(self,pObjetSoin):
        espace(1)
        print(f"Vous venez d'utiliser : {pObjetSoin.libelle}")
        self.se_soigner(pObjetSoin.puissance)
        self.enlever_objet_soin(pObjetSoin)
        espace(1)

    # Methode créer uniquement pour tester se soigner
    def perdre_PV(self,pPv):
        self.pdv -= pPv
    
    # methode se soigner qui prend en parametre un objet potion
    def se_soigner(self,PV):
        espace(1)
        if self.pdv+(PV) < self.pdvMax :
            self.pdv += PV
            print(f"Vous venez de récuperer {PV} sur {self.pdvMax}")
        elif self.pdv == self.pdvMax:
            print("Vous venez d'utiliser une Potion pour rien ! C'est dommage !")
        else:
            self.pdv = self.pdvMax
            print(f"Vous avez atteint votre santé maximum soit {self.pdvMax}")
        espace(1)
