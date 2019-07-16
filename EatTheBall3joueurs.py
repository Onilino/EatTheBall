from tkinter import*
from random import*
from tkinter.messagebox import*


scoreR = 0
scoreB = 0
scoreV = 0
scoreRX = 100
scoreBX = 100
scoreVX = 100

print ("\nJeu 3 joueurs.")

def resumme():
        print ("\nRésumé partie: ")

resumme()        

def Clavier (event):
        global PosRX, PosRY, PosBX, PosBY, PosVX, PosVY, PX, PY, scoreR, scoreB, scoreV, scoreRX, scoreBX, scoreVX
        toucheR = event.keysym
        toucheB = event.char
        toucheV = event.char


        #Déplacement rouge vers le haut

        if toucheR == "Up":
            PosRY -= 20
       
        #Déplacement rouge vers le bas

        if toucheR == "Down":
            PosRY += 20

        #Déplacement rouge la droite
                    
        if toucheR == "Right":
                PosRX += 20

        #Déplacement rouge vers la gauche

        if toucheR == "Left":
            PosRX -= 20

        #Déplacement bleu vers le haut

        if toucheB == "Z" or toucheB == "z":
            PosBY -= 20

        #Déplacement bleu vers le bas

        if toucheB == "S" or toucheB == "s":
            PosBY += 20

        #Déplacement bleu vers la droite

        if toucheB == "D" or toucheB == "d":
            PosBX += 20

        #Déplacement bleu vers la gauche

        if toucheB == "Q" or toucheB == "q":
            PosBX -= 20

        #Déplacement vert vers le haut

        if toucheV == "U" or toucheV == "u":
            PosVY -= 20

        #Déplacement vert vers le bas

        if toucheV == "J" or toucheV == "j":
            PosVY += 20

        #Déplacement vert vers la droite
                    
        if toucheV == "K" or toucheV == "k":
            PosVX += 20

        #Déplacement vert vers la gauche

        if toucheV == "H" or toucheV == "h":
            PosVX -= 20
            

        #Collision murs

        if PosRX > 1018:
            PosRX = 0
        if PosRY > 758:
            PosRY = 0
        if PosRX < 0:
            PosRX = PosRX + 1020
        if PosRY < 0:
            PosRY = PosRY + 760
        if PosBX > 1018:
            PosBX = 0
        if PosBY > 758:
            PosBY = 0
        if PosBX < 0:
            PosBX = PosBX + 1020
        if PosBY < 0:
            PosBY = PosBY + 760
        if PosVX > 1018:
            PosVX = 0
        if PosVY > 758:
            PosVY = 0
        if PosVX < 0:
            PosVX = PosVX + 1020
        if PosVY < 0:
            PosVY = PosVY + 760     


        #DEUX JOUEURS Manger la balle

        if PosRX == PX and PosRY == PY:
                    
            PX = randrange(1008)
            PX -= PX % 20
            PY = randrange(748)
            PY -= PY % 20

            scoreR += 1
            Canevas.create_text (scoreRX + (scoreR * 10), 25, text = '|', font = "Arial 20 bold")
            print ("Score rouge: ", scoreR)

        if PosBX == PX and PosBY == PY:
                    
            PX = randrange(1008)
            PX -= PX % 20
            PY = randrange(748)
            PY -= PY % 20

            scoreB += 1
            Canevas.create_text (scoreBX + (scoreB * 10), 60, text = '|', font = "Arial 20 bold")
            print ("Score bleu: ", scoreB)

        if PosVX == PX and PosVY == PY:
                    
            PX = randrange(1008)
            PX -= PX % 20
            PY = randrange(748)
            PY -= PY % 20

            scoreV += 1
                            
            Canevas.create_text (scoreVX + (scoreV * 10), 95, text = '|', font = "Arial 20 bold")
            print ("Score vert: ", scoreV)
                    
        if scoreR >= 10:
            showinfo ('Incroyable!', 'Le joueur rouge a gagné.')
            Troisjoueurs.destroy()
            print ("\nRouge: Gagné!")

        if scoreB >= 10:
            showinfo ('Incroyable!', 'Le joueur bleu a gagné.')
            Troisjoueurs.destroy()
            print ("\nBleu: Gagné!")

        if scoreV >= 10:
            showinfo ('Incroyable!', 'Le joueur vert a gagné.')
            Troisjoueurs.destroy()
            print ("\nVert: Gagné!")


        #TROIS JOUEURS Création de l'élément

        if scoreR > 10:
            Canevas.create_text (110, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (120, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (130, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (140, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (150, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (160, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (170, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (180, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (190, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (200, 25, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (110, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (120, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (130, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (140, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (150, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (160, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (170, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (180, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (190, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (200, 60, text = '|', font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (110, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (120, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (130, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (140, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (150, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (160, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (170, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (180, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (190, 95, text = "|", font = "Arial 20 bold", fill = 'white')
            Canevas.create_text (200, 95, text = "|", font = "Arial 20 bold", fill = 'white')
               
                        


        #TROIS JOUEURS On dessine le pion à sa nouvelle position

        Canevas.coords(PionR, PosRX, PosRY, PosRX + 20, PosRY + 20)
        Canevas.coords(PionB, PosBX, PosBY, PosBX + 20, PosBY + 20)
        Canevas.coords(PionV, PosVX, PosVY, PosVX + 20, PosVY + 20)
        Canevas.coords(Ball, PX , PY, PX + 20, PY + 20)


#TROIS JOUEURS Fonction restart


def restart():
                
        global PosRX, PosRY, PosBX, PosBY, PosVX, PosVY, PX, PY, scoreR, scoreB, scoreV, scoreRX, scoreBX, scoreVX
        scoreR = 0
        scoreB = 0
        scoreV = 0
        scoreRX = 100
        scoreBX = 100
        scoreVX = 100
                
                      
        PosRX = randrange (0,1008)
        PosRX -= PosRX % 20

        PosRY = randrange (0,748)
        PosRY -= PosRY % 20
                        

        PosBX = randrange (0,1008)
        PosBX -= PosBX % 20

        PosBY = randrange (0,748)
        PosBY -= PosBY % 20


        PosVX = randrange (0,1008)
        PosVX -= PosVX % 20

        PosVY = randrange (0,748)
        PosVY -= PosVY % 20


        PX = randrange (0,1008)
        PX -= PX % 20

        PY = randrange (0,748)
        PY -= PY % 20

        try:
            Canvas.delete (Canevas.create_text (110, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (120, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (130, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (140, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (150, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (160, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (170, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (180, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (190, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (200, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (110, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (120, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (130, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (140, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (150, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (160, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (170, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (180, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (190, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (200, 60, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (110, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (120, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (130, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (140, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (150, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (160, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (170, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (180, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (190, 95, text = '|', font = "Arial 20 bold", fill = 'white'),Canevas.create_text (200, 95, text = '|', font = "Arial 20 bold", fill = 'white'))
        except AttributeError:
            print ("\nNouvelle partie, 3 joueurs.")
            resumme()
            


        Canevas.coords (PionR, PosRX, PosRY, PosRX + 20, PosRY + 20)
        Canevas.coords (PionB, PosBX, PosBY, PosBX + 20, PosBY + 20)
        Canevas.coords (PionV, PosVX, PosVY, PosVX + 20, PosVY + 20)
        Canevas.coords (Ball, PX, PY, PX + 20, PY + 20)

                       
#TROIS JOUEURS Création de la fenêtre principale


Troisjoueurs = Tk()

Troisjoueurs.title ('Eat the ball 3 joueurs')

Troisjoueurs.resizable (-1,0)


#TROIS JOUEURS Position initiale du carré rouge

PosRX = randrange (0,1008)
PosRX -= PosRX % 20

PosRY = randrange (0,748)
PosRY -= PosRY % 20


#TROIS JOUEURS Position initiale du carré bleu

PosBX = randrange (0,1008)
PosBX -= PosBX % 20

PosBY = randrange (0,748)
PosBY -= PosBY % 20


#TROIS JOUEURS Position initiale du carré vert

PosVX = randrange (0,1008)
PosVX -= PosVX % 20

PosVY = randrange (0,748)
PosVY -= PosVY % 20


#DEUX JOUEURS Position initiale de la boule

PX = randrange (0,1008)
PX -= PX % 20

PY = randrange (0,748)
PY -= PY % 20




#DEUX JOUEURS Création d'un widget Canevas

Largeur = 1018
Hauteur = 758
Canevas = Canvas (Troisjoueurs, width = Largeur, height = Hauteur, bg = 'goldenrod3')
PionR = Canevas.create_rectangle (PosRX, PosRY, PosRX + 20, PosRY + 20, width = 2, outline = 'black', fill = 'red')
PionB = Canevas.create_rectangle (PosBX, PosBY, PosBX + 20, PosBY + 20, width = 2, outline = 'black', fill = 'blue')
PionV = Canevas.create_rectangle (PosVX, PosVY, PosVX + 20, PosVY + 20, width = 2, outline = 'black', fill = 'green')
Ball = Canevas.create_oval (PX, PY, PX + 20, PY + 20, width = 2, outline = 'black', fill = 'purple')

FlecheR = Canevas.create_text (1000, 364, text = '>', font = 'Arial 20 bold', fill = 'red')
FlecheR = Canevas.create_text (18, 364, text = '<', font = 'Arial 20 bold', fill = 'red')
FlecheB = Canevas.create_text (509, 25, text = '^', font = 'Arial 25 bold', fill = 'blue')
FlecheB = Canevas.create_text (509, 740, text = 'v', font = 'Arial 20 bold', fill = 'blue')


Canevas.focus_set()

Canevas.create_text (55, 25, text = "Score : ", font = "Arial 20 bold", fill = 'red')
Canevas.create_text (55, 60, text = "Score : ", font = "Arial 20 bold",fill = 'blue')
Canevas.create_text (55, 95, text = "Score : ", font = "Arial 20 bold", fill = 'green')


Canevas.create_text (110, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (120, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (130, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (140, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (150, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (160, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (170, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (180, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (190, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (200, 25, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (110, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (120, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (130, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (140, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (150, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (160, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (170, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (180, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (190, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (200, 60, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (110, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (120, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (130, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (140, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (150, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (160, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (170, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (180, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (190, 95, text = "|", font = "Arial 20 bold", fill = 'white')
Canevas.create_text (200, 95, text = "|", font = "Arial 20 bold", fill = 'white')



Canevas.bind('<KeyPress>', Clavier)
Canevas.pack(padx = 5, pady = 5)


            #TROIS JOUEURS Création de la barre d'outil FICHIER


def callback_quitter():

    if askyesno ('Attention', 'Êtes-vous sûr de vouloir quittez la partie? Votre progression sera effacée.'):
        Troisjoueurs.destroy()


def callback_nouvelle_partie():
    if askyesno ('Attention', 'Êtes-vous sûr de vouloir recommencer une partie? Votre progression sera effacée.'):
        showinfo ('Bonne chance', 'Nouvelle partie.')
        restart()


menubar = Menu (Troisjoueurs)

menu1 = Menu (menubar, tearoff = 0)
menu1.add_command (label = "Nouvelle partie", command = callback_nouvelle_partie)
menu1.add_separator()
menu1.add_command (label = "Quitter", command = callback_quitter)

menubar.add_cascade (label = "Fichier", menu = menu1)

Troisjoueurs.config (menu = menubar)



                #TROIS JOUEURS Création de la barre d'outil AIDE


def callback_regles():
    regles = Tk()
    regles.title ('Règles')
    l = LabelFrame (regles, text = "Objectif", padx = 20, pady = 20)
    l.pack (fill = "both", expand = "yes")
                         
    Label (l, text = "\nChaque joueur doit manger la boule violette.\n Le premier arrivé à 10 à gagné.\n\n\n COMMANDES JOUEUR ROUGE:\n\nAller à gauche: Flèche gauche.                         \nAller à droite: Flèche droite.                               \nAller en haut: Flèche haut.                                 \nAller en bas: Flèche bas.                                     \n\nCOMMANDES JOUEUR BLEU:\n\nAller à gauche: Q                                                 \nAller à droite: D                                                    \nAller en haut: Z                                                    \nAller en bas: S                                                       \n\nCOMMANDES JOUEUR VERT:\n\nAller à gauche: H                                                 \nAller à droite: K                                                    \nAller en haut: U                                                    \nAller en bas: J                                                       \n\nIl est interdit de rester appuyé sur une touche de direction!").pack()
    regles.mainloop()

def a_propos():
    Apropos = Tk()
    Apropos.title ('A propos')
    a = LabelFrame (Apropos, text = "Créateur", padx = 20, pady = 20)
    a.pack (fill = "both", expand = "yes")

    Label (a, text = "Eat the ball.\nEdited by Lino.\n_______________________________________\nNom: CHAUMARD      Classe: TS6                \nPrénom: Théo               Professeur: M.PENA").pack()
    Apropos.mainloop()


menu2 = Menu (menubar, tearoff = 0)
menu2.add_command (label = "Règles", command = callback_regles)
menu2.add_separator()
menu2.add_command (label = "A propos", command = a_propos)

menubar.add_cascade (label = "?", menu = menu2)

Troisjoueurs.config (menu = menubar)
                 

                #DEUX JOUEURS Création du label


label = Label (Troisjoueurs, text = "  EAT THE BALL  ", font = 'MicroMieps 20 bold', bg = 'black', fg = 'orange')
label.pack()


Troisjoueurs.mainloop()
