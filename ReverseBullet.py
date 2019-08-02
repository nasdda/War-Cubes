class ReverseBullet:
    canShoot = True

    def __init__(self,win,x,y,targetX=None,targetY=None):
        self.x = x
        self.y = y
        self.targetX = targetX
        self.targetY = targetY
        self.vel = 35

        self.diffX = targetX - x
        self.diffY = targetY - y
