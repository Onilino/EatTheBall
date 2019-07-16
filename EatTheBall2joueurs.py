from tkinter import*
from random import*
from tkinter.messagebox import*


scoreR = 0
scoreB = 0
scoreRX = 100
scoreBX = 100

print ("Jeu 2 joueurs.")

def resumme():
        print ("\nRésumé partie:")
resumme()

def Clavier (event):
        
        global PosRX, PosRY, PosBX, PosBY, PX, PY, scoreR, scoreB, scoreRX, scoreBX
        toucheR = event.keysym
        toucheB = event.char

        #DEUX JOUEURS Déplacement rouge vers le haut

        if toucheR == "Up":
            PosRY -= 20
       
        #DEUX JOUEURS Déplacement rouge vers le bas

        elif toucheR == "Down":
            PosRY += 20

        #DEUX JOUEURS Déplacement rouge la droite
                    
        elif toucheR == "Right":
                PosRX += 20

        #DEUX JOUEURS Déplacement rouge vers la gauche

        elif toucheR == "Left":
            PosRX -= 20

        #DEUX JOUEURS Déplacement bleu vers le haut

        if toucheB == "Z" or toucheB == "z":
            PosBY -= 20

        #DEUX JOUEURS Déplacement bleu vers le bas

        elif toucheB == "S" or toucheB == "s":
            PosBY += 20

        #DEUX JOUEURS Déplacement bleu vers la droite

        elif toucheB == "D" or toucheB == "d":
            PosBX += 20

        #DEUX JOUEURS Déplacement bleu vers la gauche

        elif toucheB =="Q" or toucheB == "q":
            PosBX -= 20

        #DEUX JOUEURS Collision murs

        if PosRX > 1018:

            PosRX = randrange (1)
            PosRY = PosRY

        if PosRY > 758:

            PosRX = PosRX
            PosRY = randrange (1)

        if PosRX < 0:

            PosRX = PosRX + 1020
            posRY = PosRY

        if PosRY < 0:

            PosRX = PosRX
            PosRY = PosRY + 760


        if PosBX > 1018:

            PosBX = randrange (1)
            PosBY = PosBY

        if PosBY > 758:

            PosBX = PosBX
            PosBY = randrange (1)

        if PosBX < 0:

            PosBX = PosBX + 1020
            PosBY = PosBY

        if PosBY < 0:

            PosBX = PosBX
            PosBY = PosBY + 760


        #DEUX JOUEURS Manger la balle

        if PosRX == PX and PosRY == PY:
                    
            PX = randrange (0,1008)
            PX -= PX % 20

            PY = randrange (0,748)
            PY -= PY % 20

            scoreR += 1
                            
            Canevas.create_text (scoreRX + (scoreR * 10), 25, text = '|', font = "Arial 20 bold")
            print ("Score rouge: ", scoreR)

        if PosBX == PX and PosBY == PY:
                    
            PX = randrange (0,1008)
            PX -= PX % 20

            PY = randrange (0,748)
            PY -= PY % 20

            scoreB += 1
                            
            Canevas.create_text (scoreBX + (scoreB * 10), 60, text = '|', font = "Arial 20 bold")
            print ("Score bleu: ", scoreB)

                    
        if scoreR >= 10:
            showinfo ('Incroyable!', 'Le joueur rouge a gagné.')
            Deuxjoueurs.destroy()
            print ("\nRouge: Gagné!")

        if scoreB >= 10:
            showinfo ('Incroyable!', 'Le joueur bleu a gagné.')
            Deuxjoueurs.destroy()
            print ("\nBleu: Gagné!")


        #DEUX JOUEURS Création de l'élément

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
               
                        


        #DEUX JOUEURS On dessine le pion à sa nouvelle position

        Canevas.coords (PionR, PosRX, PosRY, PosRX + 20, PosRY + 20)
        Canevas.coords (PionB, PosBX, PosBY, PosBX + 20, PosBY + 20)
        Canevas.coords (Ball, PX , PY, PX + 20, PY + 20)


#DEUX JOUEURS Fonction restart


def restart():
                
        global PosRX, PosRY, PosBX, PosBY, PX, PY, scoreR, scoreB, scoreRX, scoreBX
        scoreR = 0
        scoreB = 0
        scoreRX = 100
        scoreBX = 100
                
                      
        PosRX = randrange (0,1008)
        PosRX -= PosRX % 20

        PosRY = randrange (0,748)
        PosRY -= PosRY % 20
                        

        PosBX = randrange (0,1008)
        PosBX -= PosBX % 20

        PosBY = randrange (0,748)
        PosBY -= PosBY % 20


        PX = randrange (0,1008)
        PX -= PX % 20

        PY = randrange (0,748)
        PY -= PY % 20

        try:
            Canvas.delete (Canevas.create_text (110, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (120, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (130, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (140, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (150, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (160, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (170, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (180, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (190, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (200, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (110, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (120, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (130, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (140, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (150, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (160, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (170, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (180, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (190, 60, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (200, 60, text = '|', font = "Arial 20 bold", fill = 'white'))
        except AttributeError:
            print ("\nNouvelle partie, 2 joueurs.")
            resumme()
            

        Canevas.coords (PionR, PosRX, PosRY, PosRX + 20, PosRY + 20)
        Canevas.coords (PionB, PosBX, PosBY, PosBX + 20, PosBY + 20)
        Canevas.coords (Ball, PX, PY, PX + 20, PY + 20)

                       
#DEUX JOUEURS Création de la fenêtre principale


Deuxjoueurs = Tk()

Deuxjoueurs.title ('Eat the ball 2 joueurs')

Deuxjoueurs.resizable (-1,0)


#DEUX JOUEURS Position initiale du carré rouge

PosRX = randrange (0,1008)
PosRX -= PosRX % 20

PosRY = randrange (0,748)
PosRY -= PosRY % 20


#DEUX JOUEURS Position initiale du carré bleu

PosBX = randrange (0,1008)
PosBX -= PosBX % 20

PosBY = randrange (0,748)
PosBY -= PosBY % 20


#DEUX JOUEURS Position initiale de la boule

PX = randrange (0,1008)
PX -= PX % 20

PY = randrange (0,748)
PY -= PY % 20




#DEUX JOUEURS Création d'un widget Canevas

Largeur = 1018

Hauteur = 758

Canevas = Canvas (Deuxjoueurs, width = Largeur, height = Hauteur, bg = 'goldenrod3')

PionR = Canevas.create_rectangle (PosRX, PosRY, PosRX + 20, PosRY + 20, width = 2, outline = 'black', fill = 'red')

PionB = Canevas.create_rectangle (PosBX, PosBY, PosBX + 20, PosBY + 20, width = 2, outline = 'black', fill = 'blue')

Ball = Canevas.create_oval (PX, PY, PX + 20, PY + 20, width = 2, outline = 'black', fill = 'purple')

FlecheR = Canevas.create_text (1000, 364, text = '>', font = 'Arial 20 bold', fill = 'red')
FlecheR = Canevas.create_text (18, 364, text = '<', font = 'Arial 20 bold', fill = 'red')
FlecheB = Canevas.create_text (509, 25, text = '^', font = 'Arial 25 bold', fill = 'blue')
FlecheB = Canevas.create_text (509, 740, text = 'v', font = 'Arial 20 bold', fill = 'blue')



Canevas.focus_set()

Canevas.create_text (55, 25, text = "Score : ", font = "Arial 20 bold", fill = 'red')
Canevas.create_text (55, 60, text = "Score : ", font = "Arial 20 bold", fill = 'blue')

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


Canevas.bind ('<KeyPress>', Clavier)

Canevas.pack (padx = 5, pady = 5)


#DEUX JOUEURS Création de la barre d'outil FICHIER


def callback_quitter():

    if askyesno ('Attention', 'Êtes-vous sûr de vouloir quitter la partie? Votre progression sera effacée.'):
        Deuxjoueurs.destroy()


def callback_nouvelle_partie():
    if askyesno ('Attention', 'Êtes-vous sûr de vouloir recommencer une partie? Votre progression sera effacée.'):
        showinfo ('Bonne chance', 'Nouvelle partie.')
        restart()


menubar = Menu (Deuxjoueurs)

menu1 = Menu (menubar, tearoff = 0)
menu1.add_command (label = "Nouvelle partie", command = callback_nouvelle_partie)
menu1.add_separator()
menu1.add_command (label = "Quitter", command = callback_quitter)

menubar.add_cascade (label = "Fichier", menu = menu1)

Deuxjoueurs.config (menu = menubar)



#DEUX JOUEURS Création de la barre d'outil AIDE


def callback_regles():
    regles = Tk()
    regles.title ('Règles')
    l = LabelFrame (regles, text = "Objectif", padx = 20, pady = 20)
    l.pack (fill = "both", expand = "yes")
                         
    Label (l, text = "\nChaque joueur doit manger la boule violette,\n sans sortir du cadre. Le premier arrivé à 10 a gagné.\n\n\n COMMANDES JOUEUR ROUGE:\n\nAller à gauche: Flèche gauche.                         \nAller à droite: Flèche droite.                               \nAller en haut: Flèche haut.                                 \nAller en bas: Flèche bas.                                     \n\nCOMMANDES JOUEUR BLEU:\n\nAller à gauche: Q                                                 \nAller à droite: D                                                    \nAller en haut: Z                                                    \nAller en bas: S                                                       \n\nIl est interdit de rester appuyé sur une touche de direction!").pack()
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

Deuxjoueurs.config (menu = menubar)
                 

#DEUX JOUEURS Création du label


label = Label (Deuxjoueurs, text = "  EAT THE BALL  ", font = 'MicroMieps 20 bold', bg = 'black', fg = 'orange')
label.pack()


Deuxjoueurs.mainloop()
