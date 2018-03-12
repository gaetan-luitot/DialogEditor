# Classe "Interface", cette classe va gérer l'interface graphique :

from tkinter import *
from c_boite import *
from c_chainage import *
from c_reponse import *


# TODO :
# - Gestion des boites dans box
# - Vérifier lors de la création d'une nouvelle scène qu'il n'en n'existe pas déjà une, si c'est le cas avertire que celle ci 
#		va être supprimée : "Attention le fichier existe déjà et va être supprimé, êtes vous sur de vouloir continuer : oui / non"


class Interface:

	def __init__(self): # Constructeur :
		# Fenêtre :
		self.editor = Tk() # On créer une fenêtre "editor"
		self.editor['bg']='black' # On met le fond de couleur noir 
		self.editor.title("Editeur de Scène") # On nomme la fenêtre 
		self.editor.geometry("640x360") # On définit une taille pour la fenêtre
		self.editor.resizable(0,0) # On fixe la taille pour qu'on ne puisse pas la modifier

		# Variables :
		self.box = Boite("default")
		self.texteRep1 = StringVar() # Texte de la réponse 1 actuel
		self.texteRep2 = StringVar() # Texte de la réponse 2 actuel
		self.texteRep3 = StringVar() # Texte de la réponse 3 actuel
		self.texteDialogue = StringVar() # Texte du dialogue de la Scène ou du PNJ
		self.texteDialogue.set("[Texte]")
		self.x = 0 # x position actuel
		self.y = 0 # y position actuel
		self.pos = StringVar() # Texte de la position actuel
		self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y)) #
		self.nomFichierBoite = StringVar() # Texte de la position actuel
		self.nomFichierBoite.set("Nom du fichier")
		self.chainageActuel = Chainage(self.texteDialogue.get(), [[self.texteRep1.get(), 0, 0, False], [self.texteRep2.get(), 0, 0, False],[self.texteRep3.get(), 0, 0, False]], 0)

		
		self.Define() # On créer notre fenêtre de base
		self.LoadMenu() # On charge le menu au début
		self.Start() # On commence la boucle 

	def Start(self): # start mainloop
		self.editor.mainloop()

	def Define(self): # Création de tout les widgets de base
		# Paned Windows :
		self.X = PanedWindow(self.editor, orient = HORIZONTAL)
		self.Y = PanedWindow(self.editor, orient = HORIZONTAL)
		# Canvas :
		self.Fond = Canvas(self.editor, bg = 'black', width= 640, height = 360)
		# LabelFrame :
		self.X.add(Label(self.editor, text = '', bg = 'black', anchor = N, width = 80))
		self.Y.add(Label(self.editor, text = '', bg = 'black', anchor = N, width = 2, height = 22))
		# On affiche tout :
		self.X.grid(columnspan = 640,sticky = W)
		self.Y.grid(rowspan = 360,sticky = W)
		self.Fond.grid(rowspan = 360, columnspan = 640, row = 0, column = 0, sticky = NW)

	def LoadMenu(self):
		print("I: Chargement du menu")
		# Entry
		self.Fichier = Entry(self.editor, textvariable = self.nomFichierBoite, width = 18) # Nom du Fichier à charger ou à créer

		# Button :
		self.New = Button(self.editor, text = "Créer", command = lambda: self.NewScene(self.nomFichierBoite.get())) # Créer une nouvelle boite
		self.Load = Button(self.editor, text = "Charger", command = lambda: self.LoadScene(self.nomFichierBoite.get())) # Charger une boite déjà existante

		self.PackMenu() # On charge les éléments du Menu

	def PackMenu(self):
		# Label :
		self.Fichier.grid(columnspan = 640, rowspan = 360, row = 100, column = 150, sticky = NW)
		# Button :
		self.New.grid(columnspan = 640, rowspan = 360, row = 150, column = 150, sticky = NW)
		self.Load.grid(columnspan = 640, rowspan = 360, row = 150, column = 225, sticky = NW)

	def ClearMenu(self):
		print("I: Déchargement du menu")
		self.New.grid_forget()
		self.Load.grid_forget()
		self.Fichier.grid_forget()

	def LoadEditeur(self):
		print("I: Chargement de l'interface d'édition")
		# LabelFrame :
		self.TopHelp = Label(self.editor, text = 'Nombres de Boites :', bg = 'white', width = 20) # Help : Nombre de chainages crées
		self.TopHelpTwo = Label(self.editor, text = 'Info pour vous aider 2 :', bg = 'white', width = 20) # Help : [à définir]
		self.TexteLabel = Label(self.editor, textvariable = self.texteDialogue, bg = 'white', width = 60, height = 6, wraplength = 480, anchor = NW) # Affichage du texte écrit
		self.InfoPosVar = Label(self.editor, textvariable = self.pos, bg = 'white', width = 5, height = 2) # Help : Position actuel

		# Entry :
		self.Texte = Entry(self.editor, textvariable = self.texteDialogue, width = 60) # Texte du PNJ 
		self.Rep1 = Entry(self.editor, textvariable = self.texteRep1, width = 70) # Réponse 1 du PJ
		self.Rep2 = Entry(self.editor, textvariable = self.texteRep2, width = 70) # Réponse 2 du PJ
		self.Rep3 = Entry(self.editor, textvariable = self.texteRep3, width = 70) # Réponse 3 du PJ

		# Button :
		self.Save = Button(self.editor, text = "Save", command = self.Save) # Bouton pour sauvegarder la boite
		self.Return = Button(self.editor, text = "Return", command = self.Test) # Bouton de navigation à travers la boite : retourner en arrière
		self.ButtonRep1 = Button(self.editor, text = "Réponse 1", command = self.ApplyCurrent, width = 13) # Btn navigation : aller vers chainage suivant
		self.ButtonRep2 = Button(self.editor, text = "Réponse 2", command = self.ApplyCurrent, width = 13) # Btn navigation : aller vers chainage suivant
		self.ButtonRep3 = Button(self.editor, text = "Réponse 3", command = self.ApplyCurrent, width = 13) # Btn navigation : aller vers chainage suivant

		self.PackEditeur() # On affiche le tout
		
	def PackEditeur(self): # Update de tout les Widgets
		# UI help :
		self.TopHelp.grid(columnspan = 640, row = 0, column = 210, sticky = NW)
		self.TopHelpTwo.grid(columnspan = 640, row = 1, column = 210, sticky = NW)
		self.InfoPosVar.grid(columnspan = 640, rowspan = 360, row = 100, column = 0, sticky = NW)

		# UI Other:
		self.Save.grid(columnspan = 640, rowspan = 360, row = 0, column = 575, sticky = NW)
		self.Return.grid(columnspan = 640, rowspan = 360, row = 0, column = 0, sticky = NW)

		# Texte :
		self.Texte.grid(columnspan = 640,row = 150, column = 64, sticky = NW)
		self.TexteLabel.grid(columnspan = 640, rowspan = 360,row = 40, column = 65, sticky = NW)

		# Réponse :
		self.Rep1.grid(columnspan = 640, rowspan = 360, row = 197, column = 30, sticky = NW)
		self.Rep2.grid(columnspan = 640, rowspan = 360, row = 263, column = 30, sticky = NW)
		self.Rep3.grid(columnspan = 640, rowspan = 360, row = 328, column = 30, sticky = NW)
		self.ButtonRep1.grid(columnspan = 640, rowspan = 360, row = 160, column = 0, sticky = NW)
		self.ButtonRep2.grid(columnspan = 640, rowspan = 360, row = 226, column = 0, sticky = NW)
		self.ButtonRep3.grid(columnspan = 640, rowspan = 360, row = 291, column = 0, sticky = NW)

	def ClearEditeur(self):
		print("I: Déchargement de l'interface d'éditions")
		self.TopHelp.grid_forget()
		self.TopHelpTwo.grid_forget()
		self.InfoPosVar.grid_forget()
		self.Save.grid_forget()
		self.Return.grid_forget()
		self.Texte.grid_forget()
		self.TexteLabel.grid_forget()
		self.Rep1.grid_forget()
		self.Rep2.grid_forget()
		self.Rep3.grid_forget()
		self.ButtonRep1.grid_forget()
		self.ButtonRep2.grid_forget()
		self.ButtonRep3.grid_forget()

	def ApplyCurrent(self): # On ajoute à notre tableau box le chainage que l'on vient de créer
		self.ActualiserChainage()
		self.box.Inserer(self.chainageActuel, self.x, self.y)

	def GetCurrent(self): 
		if self.box[self.x][self.y] != None:
			self.chainageActuel = self.box[self.x][self.y]
			print(self.box[self.x][self.y].texte)
		else:
			print("E: L'index demandé n'existe pas.")

	def GoTo(self):
		self.ApplyCurrent()
		self.ActualiserWidgets()
		# Y * x+1

	def ActualiserChainage(self): # On assignent les infos rentrés dans les Entrys à notre variables chainageActuel
		listeTemporaire = []
		indexTemporaire = -1
		if self.texteRep1.get() != '':
			indexTemporaire+= 1
			listeTemporaire.append(Reponse(self.texteRep1.get(), (self.x +1), indexTemporaire))
		if self.texteRep2.get() != '':
			indexTemporaire+= 1
			listeTemporaire.append(Reponse(self.texteRep2.get(), (self.x +1), indexTemporaire))
		if self.texteRep3.get() != '':
			indexTemporaire+= 1
			listeTemporaire.append(Reponse(self.texteRep3.get(), (self.x +1), indexTemporaire))

		self.chainageActuel = Chainage(self.texteDialogue.get(), listeTemporaire, 0)

	def ActualiserWidgets(self, indexX = 0, indexY = 0): # On actualise les widgets sur un nouveau Chainage 
		try: # On essaye d'obtenir l'index :
			self.chainageActuel = self.box[indexX][indexY]
		except: # Si il n'existe pas :
			#self.chainageActuel = (Chainage.d_texte,
			print("ici") # chainageActuel.texte, chainageActuel.Reponses[0])
			# Créer une boite vierge
		else: # Si il existe :
			self.texteDialogue.set(self.chainageActuel.texte)
			if self.chainageActuel.nombreDeRep > 0:
				self.texteRep1.set(self.chainageActuel.Reponses[0].texte)
			if self.chainageActuel.nombreDeRep > 1:
				self.texteRep2.set(self.chainageActuel.Reponses[1].texte)
			if self.chainageActuel.nombreDeRep > 2:
				self.texteRep3.set(self.chainageActuel.Reponses[2].texte)
		


	def LoadScene(self, nomDuFichier):
		try:
			self.box.Load(nomDuFichier)
			print("I: Chargement du fichier " + nomDuFichier + ".save")
			self.ClearMenu()
			self.LoadEditeur()
			self.ActualiserWidgets()
		except:
			print("E: Le ficher n'existe pas !")
		

	def NewScene(self, nomDuFichier):
		self.box.New(nomDuFichier)
		self.ClearMenu()
		self.LoadEditeur()
		print("I: Création du fichier " + nomDuFichier)

	def Save(self):
		self.ApplyCurrent()
		self.box.Save()
		# print(getsizeof("Taille : " + self.box))
		print("I: Sauvegarde effectuée")

	def GoBack(self):
		self.Save() # On sauvegarde 

	def Test(self):
		return self.box.GetIndice(self.x)