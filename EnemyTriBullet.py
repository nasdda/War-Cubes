import math
import pygame

class EnemyTriBullet:
    def __init__(self,win,x,y, diffX, diffY, vel):
        self.win = win
        self.type = 't'
        self.x = x
        self.y = y
        self.x2 = x
        self.y2 = y
        self.x3 = x
        self.y3 = y
        self.diffX = diffX
        self.diffY = diffY
        self.vel = vel
        self.ang = math.atan2(diffY,diffX)


    def drawEnemyBullet(self):
        self.x += math.cos(self.ang)*self.vel
        self.y += math.sin(self.ang)*self.vel

        self.x2 += math.cos(self.ang + 0.2)*self.vel
        if self.ang < 0.5 and self.ang > -0.5:
            self.y2 += math.sin(self.ang + 0.2) * self.vel
        elif self.ang < 3 and self.ang > -3:
            self.y2 += math.sin(self.ang + 0.2) * self.vel
        else:
            self.y2 += math.sin(self.ang)*self.vel

        self.x3 += math.cos(self.ang - 0.2)*self.vel
        if self.ang < 0.5 and self.ang > -0.5:
            self.y3 += math.sin(self.ang -0.2) * self.vel
        elif self.ang < 3 and self.ang > -3:
            self.y3 += math.sin(self.ang - 0.2) * self.vel
        else:
            self.y3 += math.sin(self.ang)*self.vel

        pygame.draw.circle(self.win, (255, 93, 64), (round(self.x), round(self.y)), 7)
        pygame.draw.circle(self.win, (255, 93, 64), (round(self.x2 ), round(self.y2)), 7)
        pygame.draw.circle(self.win, (255, 93, 64), (round(self.x3), round(self.y3)), 7)