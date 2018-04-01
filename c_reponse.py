""" 
Cet classe représente une réponse que le joueur peut choisir lors d'une scène, elle contient la réponse affichée au joueur, et le chemin 
à suivre pour continuer la suite du dialogue. 
"""

from c_vecteur import Vecteur # On import notre classe Vecteur

class Reponse: # On définit notre classe, que l'on appelle "Reponse"

	def __init__(self, texte, x, z, hiden, extension = False, function = False):#, end): # Constructeur :
		self.texte = texte # La réponse que le joueur à choisi
		self.pos = Vecteur(x, z) # La position du Chainage qui répond à la réponse du PJ
		self.extend = extension
		self.hiden = hiden
		self.function = function
		
class Extension: # On définit notre classe, que l'on appelle "Reponse"

	def __init__(self, carac, difficulté, x2, z2, function = False): # Constructeur :
		self.carac = carac # 0 : Physique | 1 : Mental | 2 : Sociale 
		self.difficult = difficulté # La difficulté du jet de dés que le PJ devra battre
		self.pos2 = Vecteur(x2, z2) # La position du Chainage qui répond à la réponse du PJ
		self.function = function

		