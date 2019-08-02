import pygame
import random
import math
import time
import threading
from EnemyRegBullet import EnemyRegBullet

class RegEnemy:
    newX = 50
    newY = 50
    def __init__(self,x,y,w,h,vel):
        self.bullets = []
        self.alive = True
        self.hp = 10
        self.color = (255, 214, 102)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = vel
        self.moving = False
        self.diffX = None
        self.diffY = None
        self.fired = False


    def draw_enemy(self,win):
        self.win = win
        pygame.draw.rect(win,self.color,(self.x,self.y,self.w,self.h))


    def change_spot(self):
        if not self.moving:
            newX = random.randrange(10, 1290)
            newY = random.randrange(10, 690)
            if newX < self.x + self.vel and newX > self.x - self.vel:
                newX = random.randrange(10, 1290)
                return

            if newY < self.y + self.vel and newY > self.y - self.vel:
                newY = random.randrange(10, 690)
                return
            self.newX = newX
            self.newY = newY
            self.diffX = self.newX - self.x
            self.diffY = self.newY - self.y
            self.moving = True



    def move(self):
        if self.moving:
            ang = math.atan2(self.diffY,self.diffX)
            self.x += math.cos(ang)*self.vel
            self.y += math.sin(ang)*self.vel

        if (self.x < self.newX+self.vel and self.x > self.newX-self.vel) and (self.y < self.newY+self.vel and self.y > self.newY-self.vel):
            self.moving = False

    def pause(self,n):
        time.sleep(n)
        self.color = (255, 214, 102)

    def hit(self):
        self.color = (255,255,255)
        threading.Thread(target=self.pause, args=(0.25,)).start()

    def cool_down(self):
        time.sleep(random.randrange(2,8))
        self.fired = False

    def fire(self,win,playerX, playerY):
        if not self.fired:
            diffX = (playerX+random.randrange(-15,15)) - self.x
            diffY = (playerY+random.randrange(-15,15)) - self.y
            self.bullets.append(EnemyRegBullet(win,self.x,self.y,diffX,diffY,10))
            self.fired = True
            threading.Thread(target=self.cool_down).start()


        for bullet in self.bullets:
            bullet.drawEnemyBullet()
            if not pygame.Rect(0,0,1300,700).collidepoint(bullet.x,bullet.y):
                self.bullets.remove(bullet)






