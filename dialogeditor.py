# TO DO :
# import Tkinter 
# Is Dialog and Scene different ? 
# 
# Program's core :
#       - How do we navigate between the differents sentences ?
#   -> Perhaps, the best options is, when we create a new DialogObject, the program create a 2D Array of type "Chainage",
#      we start at the O,O position : At this moment we can create a texte, and one, two or three responses. After we have did this
#      we can click on one of this response that will bring us to the position 1,0 or 1,1 or 1,2 with the same interface. 
#
#       - What does the program return ? ( like a ".txt" file, or an object ? Maybe create our extension !? )
#   -> I think, return an object is better, because with the interface you will directly create the object, but if the program
#      return a ".txt" file the game will have to create the object himself and increase the loading periods.
#  
#       - How do we use the returned file ?
#   -> If it's an object, the game can easely use it ! With the different methods we can create in the instance 
#
# Ideas for the interface :
#       - Put a check button near the reponses, that will say to the program if these reponse put an end at the dialog or not,
#   if