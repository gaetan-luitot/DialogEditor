# Program's core :
# Ideas for the interface :
#       - Put a check label near the answers, that will say to the program if this answer put an end at the dialog or not,
#   if it is the vector of the answer will be equal to null.
#		- Make a Method to save an unfinished dialog but make sure that the exported file can't be use by the game because 
#	it can create some errors if the object is not finished. So save the file as a different object that it can't be read by the game.

# V 0.4
# -> Référence aux fonctions pour le jeu, tel réponse va lancer tel fonctions

# v 0.3
# -> Ajouter toute les strings pour une boite (mikeZ, bool, ect...)
# -> Ajouter les réponses avec un jets
# -> Fare une fonction return des vecteurs pour les x et z > 9

# v 0.2 
# -> Faire la fonction delete


from c_interface import *
from sys import getsizeof

interface = Interface()

