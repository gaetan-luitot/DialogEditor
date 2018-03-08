""" 
Cet classe regroupe 2 variables (x et y) qui correspond à une position 
"""

class Vecteur: # On définit notre classe, que l'on appelle "Vecteur" (On aurait pu l'appeller "Vecteur2D")

	def __init__(self, x, y): # Constructeur : On à besoin de deux paramètres, le x et le y à assigner à nos variables.
		self.x = x  
		self.y = y