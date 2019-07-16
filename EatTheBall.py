from tkinter import*
from random import*
from tkinter.messagebox import*

print ("Menu du jeu.")


def ClavierMENU (event):
    
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

        PosX = randrange (1)
        PosY = PosY

    if PosY > 758:

        PosX = PosX
        PosY = PosY - 760

    if PosX < 0:

        PosX = PosX + 1020
        posY = PosY

    if PosY < 0:

        PosX = PosX
        PosY = PosY + 760

    CanevasMENU.coords (Pion, PosX, PosY, PosX + 20, PosY + 20)



    #Ouvrir un des modes

    if PosX == PosX1 and PosY == PosY1:
        if askyesno ('1 joueur', 'Voulez-vous lancer une partie 1 joueur?'):

            MenuEatTheBall.destroy()

            scoreR = 0
            scoreRX = 100
            
            print ("Jeu 1 joueur.")
            
            def resumme():
                print ("\nRésumé partie:")
            resumme()

            def Clavier (event):
                
                global PosRX, PosRY, PX, PY, scoreR, scoreRX
                toucheR = event.keysym


                #UN JOUEUR Déplacement rouge vers le haut

                if toucheR == "Up":

                        PosRY -= 20


                #UN JOUEUR Déplacement rouge vers le bas

                elif toucheR == "Down":
                        PosRY += 20


                #UN JOUEUR Déplacement rouge la droite

                elif toucheR == "Right":
                        PosRX += 20


                #UN JOUEUR Déplacement rouge vers la gauche

                elif toucheR == "Left":
                        PosRX -= 20

                

                #UN JOUEUR Collision murs

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

                #UN JOUEUR Manger la balle

                if PosRX == PX and PosRY == PY:
                
                    PX = randrange (0,1008)
                    PX -= PX % 20

                    PY = randrange (0,748)
                    PY -= PY % 20

                    scoreR += 1

                   
                    Canevas.create_text (scoreRX + (scoreR * 10), 25, text = '|', font = "Arial 20 bold")
                    print ("Score rouge: ", scoreR)

                
                if scoreR >= 10:
                    showinfo ('Incroyable!', 'Le joueur rouge a gagné.')
                    Unjoueur.destroy()
                    print ("\nRouge: Gagné!")


                #UN JOUEUR Création de l'élément

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
                    


                #UN JOUEUR On dessine le pion à sa nouvelle position

                Canevas.coords (PionR, PosRX, PosRY, PosRX + 20, PosRY + 20)
                Canevas.coords (Ball, PX , PY, PX + 20, PY + 20)


            #UN JOUEUR Fonction restart

            def restart():
                
                global PosRX, PosRY, PX, PY, scoreR, scoreRX
                scoreR = 0
                scoreRX = 100
                
                
                      
                PosRX = randrange (0,1008)
                PosRX -= PosRX % 20

                PosRY = randrange (0,748)
                PosRY -= PosRY % 20


                PX = randrange (0,1008)
                PX -= PX % 20

                PY = randrange (0,748)
                PY -= P1Y % 20

                try:
                    Canvas.delete (Canevas.create_text (110, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (120, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (130, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (140, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (150, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (160, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (170, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (180, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (190, 25, text = '|', font = "Arial 20 bold", fill = 'white'), Canevas.create_text (200, 25, text = '|', font = "Arial 20 bold", fill = 'white'))
                except AttributeError:
                    print ("\nNouvelle partie")
                    resumme()


                Canevas.coords (PionR, PosRX, PosRY, PosRX + 20, PosRY + 20)
                Canevas.coords (Ball, PX, PY, PX + 20, PY + 20)

                       
            #UN JOUEUR Création de la fenêtre principale


            Unjoueur = Tk()

            Unjoueur.title ('Eat the ball 1 joueurs')

            Unjoueur.resizable (-1,0)


            #UN JOUEUR Position initiale du carré rouge

            PosRX = randrange (0,1008)
            PosRX -= PosRX % 20

            PosRY = randrange (0,748)
            PosRY -= PosRY % 20


            #UN JOUEUR Position initiale de la boule

            PX = randrange (0,1008)
            PX -= PX % 20

            PY = randrange (0,748)
            PY -= PY % 20


            #UN JOUEUR Création d'un widget Canevas

            Largeur = 1018

            Hauteur = 758

            Canevas = Canvas (Unjoueur, width = Largeur, height = Hauteur, bg = 'goldenrod3')

            PionR = Canevas.create_rectangle (PosRX, PosRY, PosRX + 20, PosRY + 20, width = 2, outline = 'black', fill = 'red')

            Ball = Canevas.create_oval (PX, PY, PX + 20, PY + 20, width = 2, outline = 'black', fill = 'purple')

            FlecheR = Canevas.create_text (1000, 364, text = '>', font = 'Arial 20 bold', fill = 'red')
            FlecheR = Canevas.create_text (18, 364, text = '<', font = 'Arial 20 bold', fill = 'red')
            FlecheB = Canevas.create_text (509, 25, text = '^', font = 'Arial 25 bold', fill = 'blue')
            FlecheB = Canevas.create_text (509, 740, text = 'v', font = 'Arial 20 bold', fill = 'blue')




            Canevas.focus_set()

            Canevas.create_text (55, 25, text = "Score : ", font = "Arial 20 bold", fill = 'red')

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


            Canevas.bind ('<KeyPress>', Clavier)

            Canevas.pack (padx = 5, pady = 5)


            #UN JOUEUR Création d'un outil FICHIER


            def callback_quitter():

                if askyesno ('Attention', 'Êtes-vous sûr de vouloir quittez la partie? Votre progression sera effacée.'):
                         Unjoueur.destroy()


            def callback_nouvelle_partie():
                    if askyesno ('Attention', 'Êtes-vous sûr de vouloir recommencer une partie? Votre progression sera effacée.'):
                        showinfo ('Bonne chance', 'Nouvelle partie.')
                        restart()


            menubar = Menu (Unjoueur)

            menu1 = Menu (menubar, tearoff = 0)
            menu1.add_command (label = "Nouvelle partie", command = callback_nouvelle_partie)
            menu1.add_separator()
            menu1.add_command (label = "Quitter", command = callback_quitter)

            menubar.add_cascade (label = "Fichier", menu = menu1)

            Unjoueur.config (menu = menubar)



            #UN JOUEUR Création d'un outil "?"

            def callback_regles():
                regles = Tk()
                regles.title ('Règles')
                l = LabelFrame (regles, text = "Objectif", padx = 20, pady = 20)
                l.pack (fill = "both", expand = "yes")
             
                Label (l, text = "\nChaque joueur doit manger la boule violette,\n sans sortir du cadre. Le premier arrivé à 10 à gagné.\n\n\n COMMANDES JOUEUR ROUGE:\n\nAller à gauche: Flèche gauche.                         \nAller à droite: Flèche droite.                               \nAller en haut: Flèche haut.                                 \nAller en bas: Flèche bas.                                     \n\nCOMMANDES JOUEUR BLEU:\n\nAller à gauche: Q                                                 \nAller à droite: D                                                    \nAller en haut: Z                                                    \nAller en bas: S                                                       \n\nCOMMANDES JOUEUR VERT:\n\nAller à gauche: H                                                 \nAller à droite: K                                                    \nAller en haut: U                                                    \nAller en bas: J                                                       \n\nIl est interdit de rester appuyé sur une touche de direction!").pack()
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

            Unjoueur.config (menu = menubar)


            #UN JOUEUR Création du label


            label = Label (Unjoueur, text = "  EAT THE BALL  ", font = 'MicroMieps 20 bold', bg = 'black', fg = 'orange')
            label.pack()


            Unjoueur.mainloop()

            

    if PosX == PosX2 and PosY == PosY2:
        if askyesno ('2 joueurs', 'Voulez-vous lancer une partie 2 joueurs?'):

            MenuEatTheBall.destroy()
        
            scoreR = 0
            scoreB = 0
            scoreBX = 100
            scoreBX = 100

            print ("Jeu 2 joueur.")
            
            def resumme(): 
                print ("\nRésummé partie:")
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
                                
                        Canevas.destroy()
                        Canevas.create_text (scoreRX + (scoreR * 10), 25, text = '|', font = "Arial 20 bold")
                        print ("Score rouge: ", scoreR)

                    if PosBX == PX and PosBY == PY:
                        
                        PX = randrange (0,1008)
                        PX -= PX % 20

                        PY = randrange (0,748)
                        PY -= PY % 20

                        scoreB += 1
                                
                        Canevas.destroy()
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


            #DEUX JOUEURS Position initiale du Food

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

                if askyesno ('Attention', 'Êtes-vous sûr de vouloir quittez la partie? Votre progression sera effacée.'):
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
                         
                Label (l, text = "\nChaque joueur doit manger la boule violette,\n sans sortir du cadre. Le premier arrivé à 10 à gagné.\n\n\n COMMANDES JOUEUR ROUGE:\n\nAller à gauche: Flèche gauche.                         \nAller à droite: Flèche droite.                               \nAller en haut: Flèche haut.                                 \nAller en bas: Flèche bas.                                     \n\nCOMMANDES JOUEUR BLEU:\n\nAller à gauche: Q                                                 \nAller à droite: D                                                    \nAller en haut: Z                                                    \nAller en bas: S                                                       \n\nCOMMANDES JOUEUR VERT:\n\nAller à gauche: H                                                 \nAller à droite: K                                                    \nAller en haut: U                                                    \nAller en bas: J                                                       \n\nIl est interdit de rester appuyé sur une touche de direction!").pack()
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


    if PosX == PosX3 and PosY == PosY3:
        if askyesno ('3 joueurs', 'Voulez-vous lancer une partie 3 joueurs?'):
            
            MenuEatTheBall.destroy()

            scoreR = 0
            scoreB = 0
            scoreV = 0
            scoreRX = 100
            scoreBX = 100
            scoreVX = 100
                        
            print ("Jeu 3 joueurs.")
            
            def resumme():
                    print ("\nRésummé partie:")
            resumme()
            
            def Clavier (event):
                    
                    global PosRX, PosRY, PosBX, PosBY, PosVX, PosVY, PX, PY, scoreR, scoreB, scoreV, scoreRX, scoreBX, scoreVX
                    toucheR = event.keysym
                    toucheB = event.char
                    toucheV = event.char


                    #TROIS JOUEURS Déplacement rouge vers le haut

                    if toucheR == "Up":
                        PosRY -= 20
                   
                    #TROIS JOUEURS Déplacement rouge vers le bas

                    elif toucheR == "Down":
                        PosRY += 20

                    #TROIS JOUEURS Déplacement rouge la droite
                                
                    elif toucheR == "Right":
                            PosRX += 20

                    #TROIS JOUEURS Déplacement rouge vers la gauche

                    elif toucheR == "Left":
                        PosRX -= 20

                        

                    #TROIS JOUEURS Déplacement bleu vers le haut

                    if toucheB == "Z" or toucheB == "z":
                        PosBY -= 20

                    #TROIS JOUEURS Déplacement bleu vers le bas

                    elif toucheB == "S" or toucheB == "s":
                        PosBY += 20

                    #TROIS JOUEURS Déplacement bleu vers la droite

                    elif toucheB == "D" or toucheB == "d":
                        PosBX += 20

                    #TROIS JOUEURS Déplacement bleu vers la gauche

                    elif toucheB == "Q" or toucheB == "q":
                        PosBX -= 20

                        

                    #TROIS JOUEURS Déplacement vert vers le haut

                    if toucheV == "U" or toucheV == "u":
                        PosVY -= 20

                    #TROIS JOUEURS Déplacement vert vers le bas

                    elif toucheV == "J" or toucheV == "j":
                        PosVY += 20

                    #TROIS JOUEURS Déplacement vert vers la droite
                                
                    elif toucheV == "K" or toucheV == "k":
                        PosVX += 20

                    #TROIS JOUEURS Déplacement vert vers la gauche

                    elif toucheV == "H" or toucheV == "h":
                        PosVX -= 20

                        

                    #TROIS JOUEURS Collision murs

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
                        
                        

                    if PosVX > 1018:

                        PosVX = randrange (1)
                        PosVY = PosVY

                    if PosVY > 758:

                        PosVX = PosVX
                        PosVY = randrange (1)

                    if PosVX < 0:

                        PosVX = PosVX + 1020
                        PosVY = PosVY

                    if PosVY < 0:

                        PosVX = PosVX
                        PosVY = PosVY + 760

                    


                    #TROIS JOUEURS Manger la balle

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

                    if PosVX == PX and PosVY == PY:
                                
                        PX = randrange (0,1008)
                        PX -= PX % 20

                        PY = randrange (0,748)
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

                    Canevas.coords (PionR, PosRX, PosRY, PosRX + 20, PosRY + 20)
                    Canevas.coords (PionB, PosBX, PosBY, PosBX + 20, PosBY + 20)
                    Canevas.coords (PionV, PosVX, PosVY, PosVX + 20, PosVY + 20)
                    Canevas.coords (Ball, PX , PY, PX + 20, PY + 20)


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


            #TROIS JOUEURS Position initiale de la boule

            PX = randrange (0,1008)
            PX -= PX % 20

            PY = randrange (0,748)
            PY -= PY % 20




            #TROIS JOUEURS Création d'un widget Canevas

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
            Canevas.create_text (55, 60, text = "Score : ", font = "Arial 20 bold", fill = 'blue')
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



            Canevas.bind ('<KeyPress>', Clavier)

            Canevas.pack (padx = 5, pady = 5)


            #TROIS JOUEURS Création de la barre d'outil FICHIER


            def callback_quitter():

                if askyesno ('Attention', 'Êtes-vous sûr de vouloir quittez la partie? Votre progression sera effacée.'):
                    Deuxjoueurs.destroy()


            def callback_nouvelle_partie():
                if askyesno ('3 joueurs', 'Voulez-vous commencer une nouvelle partie 3 joueurs?'):
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
                                     
                Label (l, text = "\nChaque joueur doit manger la boule violette,\n sans sortir du cadre. Le premier arrivé à 10 à gagné.\n\n\n COMMANDES JOUEUR ROUGE:\n\nAller à gauche: Flèche gauche.                         \nAller à droite: Flèche droite.                               \nAller en haut: Flèche haut.                                 \nAller en bas: Flèche bas.                                     \n\nCOMMANDES JOUEUR BLEU:\n\nAller à gauche: Q                                                 \nAller à droite: D                                                    \nAller en haut: Z                                                    \nAller en bas: S                                                       \n\nCOMMANDES JOUEUR VERT:\n\nAller à gauche: H                                                 \nAller à droite: K                                                    \nAller en haut: U                                                    \nAller en bas: J                                                       \n\nIl est interdit de rester appuyé sur une touche de direction!").pack()
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
                             

            #TROIS JOUEURS Création du label


            label = Label (Troisjoueurs, text = "  EAT THE BALL  ", font = 'MicroMieps 20 bold', bg = 'black', fg = 'orange')
            label.pack()


            Troisjoueurs.mainloop()



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

CanevasMENU = Canvas (MenuEatTheBall, width = Largeur, height = Hauteur, bg = 'grey10')

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


TextTitre = CanevasMENU.create_text (360, 250, text = '° EAT THE BALL °', font = 'MicroMieps 25 bold', fill = 'white')
TextAuteur = CanevasMENU.create_text (35, 750, text = '°LINO°', font = 'MicroMieps 10 bold', fill = 'white')

CanevasMENU.coords (Pion, PosX, PosY, PosX + 20, PosY + 20)

CanevasMENU.focus_set()

CanevasMENU.bind ('<KeyPress>', ClavierMENU)

CanevasMENU.pack (padx = 5, pady = 5)


    #Création de la barre d'outil FICHIER


def callback_quitterMENU():

    if askyesno ('Attention', 'Voulez-vous vraiment quitter?'):
             MenuEatTheBall.destroy()



menubarMENU = Menu (MenuEatTheBall)

menu1000 = Menu (menubarMENU, tearoff = 0)

menu1000.add_command (label = "Quitter", command = callback_quitterMENU)

menubarMENU.add_cascade (label = "Fichier", menu = menu1000)

MenuEatTheBall.config (menu = menubarMENU)



    #Création de la barre d'outil AIDE



def a_proposMENU():
    AproposMENU = Tk()
    AproposMENU.title ('A propos')
    a = LabelFrame (AproposMENU, text = "Créateur", padx = 20, pady = 20)
    a.pack (fill = "both", expand = "yes")

    Label (a, text = "Eat the ball.\nEdited by Lino.\n_______________________________________\nNom: CHAUMARD      Classe: TS6                \nPrénom: Théo               Professeur: M.PENA").pack()
    AproposMENU.mainloop()


menu2000 = Menu (menubarMENU, tearoff = 0)

menu2000.add_command (label = "A propos", command = a_proposMENU)

menubarMENU.add_cascade (label = "?", menu = menu2000)

MenuEatTheBall.config (menu = menubarMENU)


MenuEatTheBall.mainloop()
