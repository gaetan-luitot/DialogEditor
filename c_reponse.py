from c_vecteur import Vecteur

class Reponse:

	def __init__(self, texte, x, y):#, end): # Constructeur :
		self.texte = texte # La réponse du PJ
		self.pos = Vecteur(x, y) # La position de la réponse à la réponse du PJ
		#self.end = end # Est ce la fin de la scène
