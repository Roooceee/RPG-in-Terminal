from personnage import Personnage
from potion import potion

def lancer_combat(joueur, enemi):

    print(f"Un Combat est lancé entre {joueur.nom} et {enemi.nom}!")

    enemi.afficher_information()

    while joueur.pdv > 0 and enemi.pdv > 0:

        print("Que souhaitez-vous faire ?")       
        choixmenu = str(input('Appuyez sur "J" pour jouer son tour, "E" pour afficher les informations de l\'ennemi, "S" pour afficher sa santé'))
        menu = choixmenu.lower()

        if menu == "j":
            choixmenujouer= str(input('Appuyer sur "A" pour attaquer, "F" pour fuir, "I" pour ouvir Inventaire'))
            menujouer = choixmenujouer.lower()

            if menujouer == "a":
                # Ici appeler fonction attaquer de joueur
                pass

            if menujouer == "f":
                # Possibilité de rajouter un % de chance de fuite
                break

            if menujouer == "i":
                joueur.choisir_dans_inventaire_potion()

            else:
                print("Choix Invalide !")

            # Une fois que le joueur a jouer ça sera au tour de l'enemi
            # Possibilité d'implémenter le code de l'enemi ici ou 
            # Créer une fonction tour_enemi pour plus de lisibilité et de maintenabilité  

        if menu == "e":
            enemi.afficher_information()

        if menu == "s":
            joueur.afficher_sante()
        
        else:
            print("Choix Invalide !")

        



