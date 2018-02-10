import pickle

# Classe Boite :

class Boite:
	_tableau = []

	def __init__(self, nom):
		self.nom = nom # Nom du PNJ ou de la scène

	def __getitem__(self, index): # Cette méthode spéciale est appelée quand on fait objet[index]
		return self._tableau[index]

	def __setitem__(self, index, valeur): # Cette méthode est appelée quand on écrit objet[index] = valeur
		self._tableau[index] = valeur

	def __repr__(self):
		return str(self._tableau)

	def Ajouter(self, item, index):
		if index < len(self._tableau):
			self._tableau[index].append(item)
		elif index == len(self._tableau):
			self._tableau.append([item])
		else:
			print("E: Erreur l'index est trop grand !")
	
	def Inserer(self, item, indexX, indexY):
		if indexX == len(self._tableau):
			self._tableau.append([item])
		elif indexX < len(self._tableau):
			if (indexY == len(self._tableau[indexX])):
				self._tableau[indexX].append(item)
			elif (indexY < len(self._tableau[indexX])):
				self._tableau[indexX].insert(indexY, item)
			else:
				print("E: L'index Y n'existe pas")
		else:
			print("E: L'index X n'existe pas")

	def Supprimer(self, indexX, indexY):
		if indexX < len(self._tableau):
			if (indexY == 0 and indexY == len(self._tableau[indexX])-1):
				del self._tableau[indexX];
			elif (indexY < len(self._tableau[indexX])):
				del self._tableau[indexX][indexY];
			else:
				print("E: L'index Y n'existe pas")
		else:
			print("E: L'index X n'existe pas")

	def Save(self):
		with open(str(self.nom)+'.save', 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self._tableau)

	def Load(self, nom):
		with open(str(nom)+'.save', 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			boite_recupere = mon_depickler.load()
			self._tableau = boite_recupere
			self.nom = nom

	def New(self, nouveauNom):
		self._tableau = []
		self.nom = nouveauNom

	def GetYndex(self, index):
		self._tableau[index]


