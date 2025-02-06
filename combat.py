from utils import espace
import time,random


def lancer_combat(joueur, enemi):

    print(f"Un Combat est lancé entre {joueur.nom} et {enemi.nom}!")

    enemi.afficher_informations()

    while joueur.pdv > 0 and enemi.pdv > 0:

        print("Que souhaitez-vous faire ?")   
        espace(1)    
        time.sleep(1)
        choixmenu = str(input('Appuyez sur "J" pour jouer son tour, "E" pour afficher les informations de l\'ennemi, "S" pour afficher sa santé : '))
        espace(1)
        time.sleep(1)
        menu = choixmenu.lower()

        if menu == "j":
            choixmenujouer= str(input('Appuyer sur "A" pour attaquer, "F" pour fuir, "I" pour ouvir Inventaire : '))
            espace(1)
            time.sleep(1)
            menujouer = choixmenujouer.lower()

            print(f"C'est au tour de : {joueur.nom}")

            if menujouer == "a":
                joueur.attaquer(enemi)

            elif menujouer == "f":
                chiffrerandom = random.randint(1,10)
                print(chiffrerandom)
                if(chiffrerandom>3):
                    print("Fuite réussi")
                    break
                else:
                    print("Echec de la fuite !")

            elif menujouer == "i":
                joueur.choisir_dans_inventaire_potion()

            else:
                espace(1)
                time.sleep(1)
                print("Choix Invalide !")


            if(enemi.pdv>0):
                espace(1)
                time.sleep(1)
                print(f"C'est au tour de {enemi.nom}")
                enemi.attaquer(joueur)

        elif menu == "e":
            enemi.afficher_informations()

        elif menu == "s":
            joueur.afficher_sante()
        
        else:
            espace(1)
            time.sleep(1)
            print("Choix Invalide !")

        



