""" 
Cet classe regroupe 2 variables (x et z) qui correspond à une position 
"""

class Vecteur: # On définit notre classe, que l'on appelle "Vecteur"

	def __init__(self, x, z): # Constructeur -> Lors de la création d'un nouvelle objet Vecteur, on assigne des valeurs à nos variables :
		self.x = x  
		self.z = z

	def __repr__(self): # Cette fonction est appellée lorsque 
		return str("["+ str(self.x)+"] [" + str(self.z) + "]")

	def get(self):
		return str("["+ str(self.x)+"] [" + str(self.z) + "]")