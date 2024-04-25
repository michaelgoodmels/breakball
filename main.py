from gamegrid import *
from random import *

class Ball(Actor):
    def act(self):
        richtung = self.getDirection()
        if (self.getX() >= 800) or (self.getX() < 20): 
            neue_richtung = 180 - richtung 
            self.setDirection(neue_richtung) 
            self.move(5)

        if (self.getY() < 20): 
            neue_richtung = 360 - richtung 
            self.setDirection(neue_richtung) 
            self.move(5)

        if (self.getY() > 600): 
            feld.doPause() 
            msgDlg("GAME OVER")
        else:
            self.move(5)

class Brett(Actor):
    def collide(self, actor1, actor2): 
        richtung = ball.getDirection()
        neue_richtung = 360 - richtung + randint(-30, 30) 
        ball.setDirection(neue_richtung) 
        ball.move(5)
        return 0

class Block(Actor):
    def __init__(self, path): 
        Actor.__init__(self, path)
        self.setCollisionRectangle(Point(10, 10), 30, 30) 
        self.addCollisionActor(ball)

    def collide(self, actor1, actor2): 
        feld.removeActor(self) 
        feld.refresh()
        richtung = ball.getDirection() 
        neue_richtung = 360 - richtung 
        ball.setDirection(neue_richtung)
        if feld.getNumberOfActors(Block) == 0: 
            feld.doPause()
            msgDlg("Das Spiel ist gewonnen!")
        return 0

def tasteGedrueckt(tastencode): 
    xpos = brett.getX()
    if tastencode == 37:
        if xpos > 30:
            brett.setX(xpos - 5)
    elif tastencode == 39:
        if xpos < 770: 
            brett.setX(xpos + 5)

feld = GameGrid(800, 600) 
feld.setTitle("BREAKBALL") 
feld.setBgColor(Color.GRAY) 
feld.setSimulationPeriod(20) 
feld.addKeyRepeatListener(tasteGedrueckt)

ball = Ball("sprites/evalpeg_1.png") 
ball.setCollisionCircle(Point(0, 0), 10) 
feld.addActor(ball, Location(150, 300), 45)

brett = Brett("sprites/stick_1.gif") 
brett.setCollisionRectangle(Point(0, 20), 100, 2) 
brett.addCollisionActor(ball) 
feld.addActor(brett, Location(400, 580))

for xpos in range(0, 17):
    block = Block("sprites/seat_0.gif") 
    feld.addActor(block, Location(xpos * 42 + 60, 100))
    block = Block("sprites/seat_1.gif") 
    feld.addActor(block, Location(xpos * 42 + 60, 160)) 
    block = Block("sprites/seat_2.gif") 
    feld.addActor(block, Location(xpos * 42 + 60, 220))

feld.show() 
feld.doRun()