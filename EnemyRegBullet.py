import math
import pygame

class EnemyRegBullet:
    def __init__(self,win,x,y, diffX, diffY, vel):
        self.win = win
        self.type = 'r'
        self.x = x
        self.y = y
        self.diffX = diffX
        self.diffY = diffY
        self.vel = vel
        self.ang = math.atan2(diffY,diffX)

    def drawEnemyBullet(self):
        self.x += math.cos(self.ang)*self.vel
        self.y += math.sin(self.ang)*self.vel
        pygame.draw.circle(self.win,(255, 93, 64),(round(self.x),round(self.y)),7)


