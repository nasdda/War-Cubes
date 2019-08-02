import pygame
import random
import math
import time
import threading
from EnemyTriBullet import  EnemyTriBullet

class HeavyEnemy:
    newX = 50
    newY = 50
    def __init__(self,x,y,w,h,vel):
        self.bullets = []
        self.alive = True
        self.hp = 30
        self.color = (88, 84, 209)
        self.w = w
        self.h = h
        self.x = x
        self.y = y
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


    def pause(self,n):
        time.sleep(n)
        self.color = (88, 84, 209)

    def hit(self):
        self.color = (255,255,255)
        threading.Thread(target=self.pause, args=(0.25,)).start()

    def cool_down(self):
        time.sleep(random.randrange(2,6))
        self.fired = False

    def move(self):
        if self.moving:
            ang = math.atan2(self.diffY,self.diffX)
            self.x += math.cos(ang)*self.vel
            self.y += math.sin(ang)*self.vel

        if (self.x < self.newX+self.vel and self.x > self.newX-self.vel) and (self.y < self.newY+self.vel and self.y > self.newY-self.vel):
            self.moving = False

    def fire(self,win,playerX, playerY):
        if not self.fired:
            diffX = (playerX) - self.x
            diffY = (playerY) - self.y
            self.bullets.append(EnemyTriBullet(win,self.x,self.y,diffX,diffY,10))
            self.fired = True
            threading.Thread(target=self.cool_down).start()


        for bullet in self.bullets:
            bullet.drawEnemyBullet()
            if not pygame.Rect(0,0,1300,700).collidepoint(bullet.x,bullet.y) and not pygame.Rect(0,0,1300,700).collidepoint(bullet.x2,bullet.y2) and not pygame.Rect(0,0,1300,700).collidepoint(bullet.x3,bullet.y3) :
                self.bullets.remove(bullet)

