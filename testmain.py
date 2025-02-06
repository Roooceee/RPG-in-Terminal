from personnage import Personnage
from combat import lancer_combat
import random

# unPersonnageTest = Personnage('Seb',10,100,20)
# unEnemi = Personnage('Gobelin',2,30,3)

# lancer_combat(unPersonnageTest,unEnemi)

chiffrerandom = random.randint(1,10)
print(chiffrerandom)
if(chiffrerandom>3):
    print("Fuite réussi")
else:
    print("Echec de la fuite !")