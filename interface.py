# Classe "Interface", cette classe va gérer l'interface graphique :

from tkinter import *
from random import *

class Interface:

	def __init__(self): # Constructeur :
		# Fenêtre :
		self.editor = Tk() # On créer une fenêtre "editor"
		self.editor['bg']='black' # On met le fond de couleur noir 
		self.editor.title("Editeur de Scène") # On nomme la fenêtre 
		self.editor.geometry("640x360") # On définit une taille pour la fenêtre
		self.editor.resizable(0,0) # On fixe la taille pour qu'on ne puisse pas la modifier
		# Variables :
		self.value = StringVar() 
		self.value.set("texte par défaut ")

	def Define(self): # Création de tout les widgets
		# Frames :
		self.TopInfoFrame = Frame(self.editor, bg = 'white', bd = 5)
		self.TextFrame = Frame(self.editor, bg = 'white', bd = 5)
		self.LeftInfoFrame = Frame(self.editor, bg = 'white', bd = 5)
		self.RightInfoFrame = Frame(self.editor, bg = 'white', bd = 5)
		self.AnswersFrame = Frame(self.editor, bg = 'white', bd = 5)
		# Labels :self.infosX.grid()
		self.infos = Label(self.TopInfoFrame, text = "Top")
		self.texteDisplay = Label(self.TextFrame, textvariable = self.value, height = 4, wraplength = 480, bg = 'white', anchor = N)
		self.infNowText = Label(self.LeftInfoFrame, text = "x : \ny:")
		self.infNowXY = Label(self.LeftInfoFrame, text = "4 \n5")
		self.infos3 = Label(self.AnswersFrame, text = "Answers")
		self.infos4 = Label(self.RightInfoFrame, text = "Some Button")
		# Entry :
		self.texte = Entry(self.TextFrame, textvariable = self.value, width= 60)


	def PackAll(self): # Update des Widgets
		self.TopInfoFrame.grid(row=0, column=1)
		self.infos.grid()
		self.infNowText.grid()
		self.infNowXY.grid()
		self.infos3.grid()
		self.infos4.grid()
		self.TextFrame.grid(row=1, column=1, columnspan = 3)
		self.LeftInfoFrame.grid(row=1, column=0)
		self.RightInfoFrame.grid(row=1, column=5)
		self.AnswersFrame.grid(row = 2, column = 1)
		self.texte.grid(ipady = 10)
		self.texteDisplay.grid()

	def Start(self): # start mainloop
		self.editor.mainloop()


interface = Interface()
interface.Define()
interface.PackAll()
interface.Start()


