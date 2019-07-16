from tkinter import*
from random import*
from tkinter.messagebox import*

print("Menu du jeu.")

def Clavier(event):
    
    global PosX, PosY
    touche = event.keysym

    #Déplacement rouge vers le haut

    if touche == "Up":
        PosY -= 20

    #Déplacement rouge vers le bas

    elif touche == "Down":
        PosY += 20

    #Déplacement rouge la droite

    elif touche == "Right":
        PosX += 20

    #Déplacement rouge vers la gauche

    elif touche == "Left":
        PosX -= 20

    #Collision murs

    if PosX > 1018:
        PosX = 0
    if PosY > 758:
        PosY = PosY - 760
    if PosX < 0:
        PosX = PosX + 1020
    if PosY < 0:
        PosY = PosY + 760
    CanevasMENU.coords(Pion, PosX, PosY, PosX + 20, PosY + 20)

    #Ouvrir un des modes

    if PosX == PosX1 and PosY == PosY1:
        print("Jeu 1 joueur.")

    if PosX == PosX3 and PosY == PosY2:
        print("Jeu 2 joueurs.")

    if PosX == PosX3 and PosY == PosY3:
        print("Jeu 3 joueurs.")

#Création de la fenêtre principale


MenuEatTheBall = Tk()
MenuEatTheBall.title ('Eat the ball menu')
MenuEatTheBall.resizable (-1,0)


    #Position initiale du carré rouge

PosX = 200
PosY = 364


    #Position initiale du carré 1 joueur

PosX1 = 640
PosY1 = 164

    #Position initiale du carré 2 joueurs

PosX2 = 640
PosY2 = 364

    #Position initiale du carré 3 joueurs

PosX3 = 640
PosY3 = 564

    #Création d'un widget Canevas

Largeur = 1018
Hauteur = 758

CanevasMENU = Canvas (MenuEatTheBall, width = Largeur, height = Hauteur, bg = 'black')

Pion = CanevasMENU.create_rectangle (PosX, PosY, PosX + 20, PosY + 20, width = 2, outline = 'cyan', fill = 'red')
Pion1 = CanevasMENU.create_rectangle (PosX1, PosY1, PosX1 + 20, PosY1 + 20, width = 2, outline = 'white')
Pion2 = CanevasMENU.create_rectangle (PosX2, PosY2, PosX2 + 20, PosY2 + 20, width = 2, outline = 'white')
Pion3 = CanevasMENU.create_rectangle (PosX3, PosY3, PosX3 + 20, PosY3 + 20, width = 2, outline = 'white')

Text1 = CanevasMENU.create_text (775, 163, text = '1 JOUEUR', font = 'Micro 50 bold', fill = 'red')
Text2 = CanevasMENU.create_text (736, 363, text = '2 JOU', font = 'Micro 50 bold', fill = 'red')
Text2 = CanevasMENU.create_text (869, 363, text = 'EURS', font = 'Micro 50 bold', fill = 'blue')

Text3 = CanevasMENU.create_text (720, 563, text = '3 JO', font = 'Micro 50 bold', fill = 'red')
Text3 = CanevasMENU.create_text (808, 563, text = 'UE', font = 'Micro 50 bold', fill = 'blue')
Text3 = CanevasMENU.create_text (882, 563, text = 'URS', font = 'Micro 50 bold', fill = 'green')

TextTitre = CanevasMENU.create_text (375, 250, text = '°EAT THE BALL°', font = 'MicroMieps 25 bold', fill = 'white')
TextAuteur = CanevasMENU.create_text (35, 750, text = '°LINO°', font = 'MicroMieps 10 bold', fill = 'white')
CanevasMENU.coords (Pion, PosX, PosY, PosX + 20, PosY + 20)
CanevasMENU.focus_set()
CanevasMENU.bind ('<KeyPress>', Clavier)
CanevasMENU.pack (padx = 5, pady = 5)

    #Création de la barre d'outil FICHIER

def callback_quitter():
    if askyesno('Attention', 'Voulez-vous vraiment quitter?'):
        MenuEatTheBall.destroy()

menubar = Menu (MenuEatTheBall)
menu1000 = Menu (menubar, tearoff = 0)
menu1000.add_command (label = "Quitter", command = callback_quitter)
menubar.add_cascade (label = "Fichier", menu = menu1000)
MenuEatTheBall.config (menu = menubar)

    #Création de la barre d'outil "?"

def a_propos():
    Apropos = Tk()
    Apropos.title ('A propos')
    a = LabelFrame (Apropos, text = "Créateur", padx = 20, pady = 20)
    a.pack (fill = "both", expand = "yes")

    Label (a, text = "Eat the ball.\nEdited by Lino.\n_______________________________________\nNom: CHAUMARD      Classe: TS6                \nPrénom: Théo               Professeur: M.PENA").pack()
    Apropos.mainloop()


menu2000 = Menu (menubar, tearoff = 0)
menu2000.add_command (label = "A propos", command = a_propos)
menubar.add_cascade (label = "?", menu = menu2000)
MenuEatTheBall.config (menu = menubar)
MenuEatTheBall.mainloop()
