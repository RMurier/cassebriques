import pyxel

class Jeu(object):
    def __init__(self):
        """
        initialisation du Jeu
        """
        self.x = self.y = 150
        pyxel.init(self.x, self.y, title="Broke bricks | Romain / Amand")
        pyxel.load("src/assets/brokebriks.pyxres")
        self.ball = Ball()
        self.racket = Racket()
        self.bricks = GroupBrick()
        pyxel.run(self.update, self.draw)

    def update(self):
        """Mise à jour des variables (30 fPS)"""
        self.racket.movement(self.x)
        self.ball.movement(self.racket, self.x, self.y)

    def draw(self):
        """Création et positionnement des objets (30fps)"""
        pyxel.cls(0)
        self.racket.draw()
        self.ball.draw()


class Racket(object):
    def __init__(self):
        self.x = 50

    def movement(self, x):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < x-18:
            self.x += 2.3
            
        elif pyxel.btn(pyxel.KEY_LEFT) and self.x-2 > 0:
            self.x -= 2.3
        
    def draw(self):
        pyxel.blt(self.x, 115, 0, 0, 6, 16, 6)
            
class GroupBrick(object):
    def __init__(self):
        self.lstBriques = [Brick() for i in range(0, 10)]

    def draw(self):
        """
        Création et positionnement des objets (30fps)
        """
        


class Brick(object):
    def __init__(self):
        self.brick_x = 60
        self.brick_y = 60

    def draw(self):
        """
        Création et positionnement des objets (30fps)
        """
        pyxel.blt(20, 20, 0, 0, 0, 16, 16)


class Ball(object):
    def __init__(self):
        self.x = 60
        self.y = 60
        self.valX = 0
        self.valY = 1
    
    def movement(self, racket, winX, winY):
        if racket.x <= self.x + 3 and 115 <= self.y + 3 and racket.x+14 >= self.x and 115 >= self.y:
            if self.valX == 0:
                self.valX = 1
            else: 
                if pyxel.btn(pyxel.KEY_RIGHT):
                    self.valX = 1
                elif pyxel.btn(pyxel.KEY_LEFT):
                    self.valX = -1
            self.valY = -self.valY
            
        if self.y == 0:
            self.valY = -self.valY
        elif self.y > winY:
            self.x = self.y = 60
            self.valY = 1
            self.valX = 0
            
        if self.x == 0 or self.x == winX:
             self.valX = -self.valX
            
        self.y += self.valY
        self.x += self.valX

    def collision(self, brick):
        pass
    
    def draw(self):
        """Création et positionnement des objets (30fps)"""
        pyxel.circ(self.x, self.y, 2, 6)
        pyxel.circb(self.x, self.y, 2, 9)

if __name__ == '__main__':
    Jeu()
