""" 
Cet classe représente une réponse que le joueur peut choisir lors d'une scène, elle contient la réponse affichée au joueur, et le chemin 
à suivre pour continuer la suite du dialogue. 
"""

from c_vecteur import Vecteur # On import notre classe Vecteur

class Reponse: # On définit notre classe, que l'on appelle "Reponse"

	def __init__(self, texte, x, z):#, end): # Constructeur :
		self.texte = texte # La réponse que le joueur à choisi
		self.pos = Vecteur(x, z) # La position du Chainage qui répond à la réponse du PJ
		#self.end = end # Est ce la fin de la scène

