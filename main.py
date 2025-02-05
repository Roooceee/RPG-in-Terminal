from personnage import Personnage
from utils import espace
import time,random

# On demande au joueur de choisir un nom
name_player = str(input("Veuillez entrer votre nom : "))
espace(1)
# On crée un joueur avec les informations demandées
player = Personnage(name_player, 1, 100, 8)
# On affiche les infos de notre personnage
player.afficher_informations()

# On attend encore 1 seconde
time.sleep(1)
# On créé un personnage non joueur avec les informations ci-dessous
pnj = Personnage("Bob", 2, 80, 7)

# On affiche "Un nouveau joueur rejoint votre groupe."
print("Un nouveau joueur rejoint le groupe.")

listCoop = [
        player,
        pnj
    ]

print("Affichage des infos du groupe !")
for i in listCoop:
    i.afficher_informations()
    # on affiche les informations des Personnage compostant le groupe 

player.choisir_dans_inventaire()

# On attend 2 secondes pour l'affichage dans le terminal
# time.sleep(2)
# On affiche que le joueur part à l'aventure avec le PNJ
print(f"{player.nom} part à l'aventure avec {pnj.nom}.")
# On attend 4 seconde
time.sleep(2)
# Oh non, les joueurs rencontrent un ennemi !
enemy = Personnage("Gobelin", 3, 40, 3)

# On laisse au joueur la possibilité de :
# Appuyer sur "A" pour attaquer
# Appuyer sur "F" pour fuir
# Appuyer sur "I" pour afficher les informations de l'ennemi

print(f"Oh non ! Vous êtes tombé sur un ennemi, mais, c'est... un {enemy.nom}.")
time.sleep(1)

while player.pdv > 0 and enemy.pdv > 0:

    espace(1)
    print("Que souhaitez-vous faire ?")
    choixmenu = str(input('Appuyez sur "A" pour attaquer, "F" pour fuir, "E" pour afficher les informations de l\'ennemi, "T" pour afficher les stats du groupe , "I" pour ouvrir l\'inventaire'))
    menu = choixmenu.lower()

    if menu == "a":

        player.attaquer(enemy)
        time.sleep(1)

        pnj.attaquer(enemy)
        time.sleep(1)

        # vu que l'on a attaqué l'ennemi attaque
        enemyAttackPlayerRandom = random.choice(listCoop)
        print(enemyAttackPlayerRandom.nom)
        enemy.attaquer(enemyAttackPlayerRandom)

    if menu =="f":
        break

    if menu =="e":
        # affiche les infos de l'ennemi
        enemy.afficher_informations()

    if menu =="I":
        player.afficher_inventaire()


    if menu == "t":
        # affiche les infos du groupe
        for i in listCoop:
            i.afficher_informations()

