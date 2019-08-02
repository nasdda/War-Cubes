import sys
import pygame
from player import player
from RegBullet import RegBullet
import time
import threading
import math
from ReverseBullet import ReverseBullet
from enemy import RegEnemy
from HeavyEnemy import HeavyEnemy
from EnemyRegBullet import EnemyRegBullet
import random

def text_objects(text, font):
    textSurface = font.render(text, True, (171, 175, 179))
    return textSurface, textSurface.get_rect()

show = True
player_dead = False

def stage_count_timer(n):
    time.sleep(n)
    global show
    show = False

win = pygame.display.set_mode((1300, 750))
def run_game(stage):
    def show_stage(stage):
        textFont = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects(f'Stage {stage}', textFont)
        TextRect.center = ((1300 / 2), (700 / 2))
        win.blit(TextSurf,TextRect)

    threading.Thread(target=stage_count_timer,args=(3,)).start()

    p1 = player(win,600,600,30,30,5,(135,230,130))
    regBullets = []
    reverseBullets = []
    enemyList = []
    pygame.init()
    pygame.display.set_caption("War Cubes")
    bg = pygame.image.load("background.jpg")
    bg = pygame.transform.scale(bg,(1300,750))
    clock = pygame.time.Clock()

    def spawn_enemy(r,h):
        for i in range(r):
            x = random.randrange(0,1200)
            y =  random.randrange(0, 500)
            enemyList.append(RegEnemy(x, y, 40, 40, 5))
            time.sleep(1)

        for i in range(h):
            x = random.randrange(0,1200)
            y =  random.randrange(0, 500)
            enemyList.append(HeavyEnemy(x, y, 50, 50, 3))

    round_stage = {1:[3,0],2:[5,1],3:[8,2]}
    difficulty = round_stage.get(stage,'end') #gets difficulty level depending on stage number
    if difficulty == 'end':
        p1.incVel(-p1.getVel())
        regBullets.clear()
        reverseBullets.clear()
        stage = 'Complete!'
        show_stage(stage)
        pygame.display.update()
        pygame.quit()
        sys.exit()

    pygame.time.delay(10)
    threading.Thread(target=spawn_enemy,args=(difficulty[0],difficulty[1])).start()
    def shootReg(bullets):
        for bullet in bullets:
            if pygame.Rect(0,0,1300,700).collidepoint(bullet.x,bullet.y):
                for e in enemyList:
                    if pygame.Rect(e.x,e.y,e.w+5,e.h+5).collidepoint(bullet.x,bullet.y) and e.alive:
                        if bullet in regBullets:
                            regBullets.remove(bullet)
                        e.hit()
                        e.hp -= 1
                        if e.hp <= 0:
                            e.alive = False

                pygame.draw.circle(win, (255, 255, 255), (round(bullet.x) ,round(bullet.y)),5)
                ang = math.atan2(bullet.diffY,bullet.diffX)
                bullet.x += math.cos(ang)*bullet.vel
                bullet.y += math.sin(ang)*bullet.vel
            elif not pygame.Rect(0,0,1300,700).collidepoint(bullet.x,bullet.y):
                if bullet in regBullets:
                    regBullets.remove(bullet)


    def shootReverse(bullets):
        for bullet in bullets:
            if pygame.Rect(0,0,1300,700).collidepoint(bullet.x,bullet.y):
                for e in enemyList:
                    if pygame.Rect(e.x,e.y,e.w+5,e.h+5).collidepoint(bullet.x,bullet.y) and e.alive:
                        if bullet in regBullets:
                            reverseBullets.remove(bullet)
                        e.hit()
                        e.hp -= 1
                        if e.hp <= 0:
                            e.alive = False

                pygame.draw.circle(win, (255, 255, 255), (round(bullet.x) ,round(bullet.y)),5)
                ang = math.atan2(bullet.diffY,bullet.diffX)
                bullet.x -= math.cos(ang)*bullet.vel
                bullet.y -= math.sin(ang)*bullet.vel
            elif not pygame.Rect(0,0,1300,700).collidepoint(bullet.x,bullet.y):
                if bullet in regBullets:
                    reverseBullets.remove(bullet)



    def cool_down(type,pauseTime):
        countDownTime = pauseTime
        while countDownTime > 0:
            countDownTime -= 1
            time.sleep(0.1)
        type.canShoot = True

    def check_hit():
        for e in enemyList:
            for bullet in e.bullets:
                if  bullet.type == 'r':
                    if pygame.Rect(p1.getX(), p1.getY(), p1.getW(), p1.getH()).collidepoint(bullet.x, bullet.y):
                        p1.hp -= 5
                        e.bullets.remove(bullet)
                        threading.Thread(target=p1.hit).start()

                elif bullet.type == 't':
                    if pygame.Rect(p1.getX(), p1.getY(), p1.getW(), p1.getH()).collidepoint(bullet.x, bullet.y)  or \
                        pygame.Rect(p1.getX(), p1.getY(), p1.getW(), p1.getH()).collidepoint(bullet.x2, bullet.y2) or\
                        pygame.Rect(p1.getX(), p1.getY(), p1.getW(), p1.getH()).collidepoint(bullet.x3, bullet.y3):
                            p1.hp -= 7
                            e.bullets.remove(bullet)
                            threading.Thread(target=p1.hit).start()

    def checkHP():
        if(p1.hp <= 0):
            global  player_dead
            player_dead = True
            win.blit(bg, (0, 0))
            stage = 'Failed'
            show_stage(stage)
            pygame.display.update()




#########################################################################

    def drawWindow():
        win.blit(bg,(0,0))
        if show:
            show_stage(stage)
        pygame.draw.rect(win,p1.color,(p1.getX(),p1.getY(),p1.getW(),p1.getH()))
        shootReg(regBullets)
        shootReverse(reverseBullets)
        for e in enemyList:
            if e.alive:
                e.draw_enemy(win)
                e.fire(win,p1.getX(),p1.getY())

        p1.draw_hp(win)
        pygame.display.update()
        clock.tick(30)

    ##### main loop #####
    run = True
    pygame.time.delay(100)
    while run:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        for enemy in enemyList:
            if enemy.alive:
                enemy.change_spot()
                enemy.move()
            else:
                enemyList.remove(enemy)

        check_hit()

        checkHP()

        if not player_dead:
            drawWindow()

        keys = pygame.key.get_pressed()

        ##### player bullets #####
        if keys[pygame.K_q] and RegBullet.canShoot:
            RegBullet.canShoot = False
            regBullets.append(RegBullet(win,x=p1.getX()+p1.getW()//2,y=p1.getY()+p1.getH()//2,targetX=pos[0],targetY=pos[1]))
            pause = threading.Thread(target=cool_down,args=(RegBullet,1))
            pause.start()
        if keys[pygame.K_w] and ReverseBullet.canShoot:
            ReverseBullet.canShoot = False
            reverseBullets.append(ReverseBullet(win,x=p1.getX()+p1.getW()//2,y=p1.getY()+p1.getH()//2,targetX=pos[0],targetY=pos[1]))
            pause = threading.Thread(target=cool_down,args=(ReverseBullet,1))
            pause.start()
            

        ##### player movement #####
        if pygame.mouse.get_pressed()[0]:
            p1.move(pos)

        if not enemyList:
            break

stage = 0
while True:
    stage += 1 #increase stage number each time the previous stage is cleared
    show = True
    run_game(stage)
