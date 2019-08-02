import pygame
import time
class player:
    def __init__(self,win,x,y,w,h,vel,color):
        #Unnecessary to use private variables here. Just practicing encapsulation
        self.alive = True
        self.hp = 100
        self.win = win
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__vel = vel
        self.color = color
        self.originalColor = color

    #Setters
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getW(self):
        return self.__w

    def getH(self):
        return self.__h

    def getVel(self):
        return self.__vel


    #Increment
    def incX(self, n):
        self.__x += n

    def incY(self, n):
        self.__y += n

    def incVel(self, n):
        self.__vel += n



    ##### player movement #####
    def move(self,pos):
        if pos[0] > self.getX() + self.getW():
            self.incX(self.getVel())
        if pos[0] < self.getX() + self.getW():
            self.incX(-self.getVel())
        if pos[1] > self.getY() + self.getH() and self.getY() + self.getH()//2 < 700:
            self.incY(self.getVel())
        if pos[1] < self.getY() + self.getW():
            self.incY(-self.getVel())

    def text_objects(self,text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()

    def hpText(self,win):
        textFont = pygame.font.Font('freesansbold.ttf', 18)
        TextSurf, TextRect = self.text_objects('HP', textFont)
        TextRect.center = ((530), (730))
        win.blit(TextSurf, TextRect)

    def draw_hp(self,win):
        width = round(200 * (self.hp / 100))
        height = 20
        pygame.draw.rect(win, (247, 62, 62), (550, 720, 200, 20))
        pygame.draw.rect(win,(122, 230, 125),(550,720,width,height))
        self.hpText(win)



    def hit(self):
        for i in range(2):
            self.color = (255, 28, 28)
            time.sleep(0.1)
            self.color = self.originalColor





