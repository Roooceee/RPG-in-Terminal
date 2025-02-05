from personnage import Personnage
from utils import espace
import time,random

unPersonnageTest = Personnage('Seb',10,100,20)
unPersonnageTest.perdre_PV(30)
unPersonnageTest.choisir_dans_inventaire_potion()
unPersonnageTest.afficher_informations()