"""
Cet classe représente une Boite du dialogue, une phrase avec plusieurs Réponses
"""

from c_reponse import Reponse # On importe notre classe Reponse

class Chainage: # On définit notre classe, que l'on appelle "Chainage"

	d_texte = "[Texte]" # variable static qui contient le texte par défaut
	d_Reponses = [Reponse("", 1, 0),Reponse("", 1, 1), Reponse("", 1, 2)] # tableau static d'object qui contient les réponses par défaut

	def __init__(self, texte, ReponsesArray, indice = 0): # Constructeur qui prend en paramètre la phrase et le tableau de réponses
		self.indice = indice
		self.texte = texte # Phrase du PNJ ou du narateur
		self.Reponses = ReponsesArray # Tableau = [Reponse(), Reponse(), Reponse()] Contient les différentes réponses possible du joueur
		self.nombreDeRep = len(ReponsesArray) # Représente le nombre de réponses
