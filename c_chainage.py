from c_reponse import Reponse

class Chainage: # Instance d'une Boite du dialogue ( Une phrase vaec plusieurs réponses)
	def __init__(self, texte, ReponsesArray):
		self.texte = texte # Phrase du PNJ ou du narateur
		self.Reponses = ReponsesArray # Tableau = [Reponse(), Reponse(), Reponse()] Contient les différentes réponse possible du joueur
		self.nombreDeRep = len(ReponsesArray) # Représente le nombre de réponses

"""test = Chainage("test", 2, Reponse("Hello", 6, 7, False))
print(test.texte, test.nombreDeRep, test.Reponses.texte)"""