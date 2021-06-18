#Lors d'un mouvement, l'ensemble des tuiles du plateau sont déplacés dans la même direction jusqu'à rencontrer les bords du plateau ou une autre tuile sur leur chemin.
#Si deux tuiles, ayant le même nombre, entrent en collision durant le mouvement,
#elles fusionnent en une nouvelle tuile de valeur double (par ex. : deux tuiles de valeur « 2 » donnent une tuile de valeur « 4 »).
#À chaque mouvement, une tuile portant un 2 ou un 4 apparaît dans une case vide de manière aléatoire.

from tkinter import *
from random import *
from time import *

class Carré(Canvas):
    def __init__(self, master, posx = 0, posy = 0, **options):
        Canvas.__init__(self, master, bg = "white",width = 100, height = 100, **options)
        self.nb = 0
        self.posx, self.posy = posx, posy
        self.text = self.create_text(float(self["width"])/2, float(self["height"])/2, text = " ")
        self.master = master

    def change(self, nb):
        self.nb = nb

        if self.nb == 2:
            self["bg"] = '#e4e6cc'
        elif self.nb == 4:
            self["bg"] = '#b8b692'
        elif self.nb == 8:
            self["bg"] = '#cb9d6b'
        elif self.nb == 16:
            self["bg"] = '#d97e68'
        elif self.nb == 32:
            self["bg"] = '#fe5c2e'
        elif self.nb == 64:
            self["bg"] = '#ff1a1a'
        elif self.nb == 128:
            self["bg"] = '#e7d674'
        elif self.nb == 256:
            self["bg"] = '#d0d26f'
        elif self.nb == 512:
            self["bg"] = '#ffff00'
        elif self.nb == 1024:
            self["bg"] = '#8888ff'
        elif self.nb == 2048:
            self["bg"] = '#0000ff'
        else:
            self["bg"] = 'white'

        if self.nb != 0:
            self.itemconfig(self.text, text = str(self.nb))
        else:
            self.itemconfig(self.text, text = " ")

        self.update()

class fen2048(Frame):
    def __init__(self, master, time = 0.05, **options):
        Frame.__init__(self, master,width = 400, height = 400, **options)
        self.master = master
        self.time = time

        self.focus_set()

        self.bind("<Up>", self.clavierup)
        self.bind("<Down>", self.clavierdown)
        self.bind("<Left>", self.clavierleft)
        self.bind("<Right>", self.clavierright)

        self.list = []
        for x in range(0,4):
            self.list.append([])
            for y in range(0,4):
                carré = Carré(self, posx = x, posy = y)
                carré.grid(column = x, row = y)
                self.list[x].append(carré)
        self.clavier()

    def clavier(self):
        end = True
        for essai in range(1000):
            carré = self.list[randint(0,3)][randint(0,3)]
            if carré.nb == 0:
                carré.change(randint(1,2)*2)
                end = False
                break
        if end == True:
            print("GAME OVER...")
            sleep(5)
            quit()

    def clavierup(self,event):
        for t in range(3):
                for x in range(0,4):
                    for y in range(0,4):
                        carré = self.list[x][y]
                        if carré.nb != 0 and y != 0 and self.list[x][y-1].nb == 0:
                            self.list[x][y-1].change(carré.nb)
                            carré.change(0)
                        try:
                            if self.list[x][y-1].nb == carré.nb:
                                self.list[x][y-1].change(carré.nb*2)
                                carré.change(0)
                        except IndexError:
                            pass
                sleep(self.time)

        self.clavier()

    def clavierdown(self,event):
        for t in range(3):
                for x in range(0,4):
                    for y in range(0,4):
                        carré = self.list[x][y]
                        if carré.nb != 0 and y != 3 and self.list[x][y+1].nb == 0:
                            self.list[x][y+1].change(carré.nb)
                            carré.change(0)
                        try:
                            if self.list[x][y+1].nb == carré.nb:
                                self.list[x][y+1].change(carré.nb*2)
                                carré.change(0)
                        except IndexError:
                            pass
                sleep(self.time)
        self.clavier()

    def clavierleft(self,event):
        for t in range(3):
                for x in range(0,4):
                    for y in range(0,4):
                        carré = self.list[x][y]
                        if carré.nb != 0 and x != 0 and self.list[x-1][y].nb == 0:
                            self.list[x-1][y].change(carré.nb)
                            carré.change(0)
                        try:
                            if self.list[x-1][y].nb == carré.nb:
                                self.list[x-1][y].change(carré.nb*2)
                                carré.change(0)
                        except IndexError:
                            pass
                sleep(self.time)
        self.clavier()

    def clavierright(self,event):
        for t in range(3):
                for x in range(0,4):
                    for y in range(0,4):
                        carré = self.list[x][y]
                        if carré.nb != 0 and x != 3 and self.list[x+1][y].nb == 0:
                            self.list[x+1][y].change(carré.nb)
                            carré.change(0)
                        try:
                            if self.list[x+1][y].nb == carré.nb:
                                self.list[x+1][y].change(carré.nb*2)
                                carré.change(0)
                        except IndexError:
                            pass
                sleep(self.time)
        self.clavier()

if __name__ == "__main__":
    fen = Tk()
    fen.title("un petit 2048 ")
    mainfen = fen2048(fen)
    mainfen.pack(expand = 1)
    fen.mainloop()

