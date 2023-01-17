import pygame as pg
import random
import sys
from time import sleep
import schedule

hp = 2
inv = False
inv_time_s = 0

class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    speed = 10
    bounce = 24
    gun_offset = -11

    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.reloading = 0
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def gunpos(self):
        pos =  self.gun_offset + self.rct.centerx
        return pos, self.rct.top

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = 0
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        self.blit(scr)


#追加機能：音楽
def sound():                                        
    pg.mixer.init(frequency = 44100)
    pg.mixer.music.load("../fig/NES-Shooter-C04-1(Stage3).mp3")
    pg.mixer.music.play(1)

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def p_inv(inv):
    if inv > 0:
        inv = inv-1
    return



def main():
    clock =pg.time.Clock()
<<<<<<< HEAD
    scr = Screen("負けるな！こうかとん", (1200,700), "../fig/6.jpg")
=======
    scr = Screen("弾幕こうかとん", (1200,700), "../fig/side02.jpg")
>>>>>>> 492fbd04a59df5ac44c47bf670739b7c040cd039
    kkt = Bird("../fig/3.png", 1.0, (600,650))
    kkt.update(scr)

    # 追加機能：弾幕
    sleep(3) #3秒待つ
    bkd_lst = []
    def mk_bomb(scr:Screen):
        colors = ["red","orange","yellow","green","light blue","blue","purple"]
        for i in range(7):
            color = colors[i]
            vx = random.choice([-1,+1])
            vy = random.choice([-1,+1])
            bkd = Bomb(color, 10, (vx, vy),scr)
            bkd_lst.append(bkd)
    schedule.every(0.5).seconds.do(mk_bomb,scr=scr) #0.5秒に一回動作する
    
    while True:        
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        kkt.update(scr)

        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_t]:
            pg.time.wait(1000)

        for bomb in bkd_lst:
            bomb.update(scr)
            if kkt.rct.colliderect(bomb.rct):
                global hp
                if not inv:
                    hp = hp-1
                    inv_time_s = pg.time.get_ticks()
                    inv = True
                    
                if inv:
                    inv_time_e = pg.time.get_ticks()
                    if inv_time_e - inv_time_s > 2000:
                        inv = False
                #追加機能：Game Over
                if hp ==0:
                    pg.mixer.music.stop()
                    tori_sfc = pg.image.load("../fig/8.png")
                    tori_sfc = pg.transform.rotozoom(tori_sfc, 0,8.0)
                    tori_rct = tori_sfc.get_rect()
                    tori_rct.center = 600,350
                    scr.sfc.blit(tori_sfc,tori_rct)
                    fonto = pg.font.Font(None,80)
                    text = fonto.render("Game Over",True,"RED")
                    scr.sfc.blit(text,(400,200))
                    pg.display.update()
                    clock.tick(1)  
                    return
        
        schedule.run_pending() #スケジュールを行う
        pg.display.update()
        clock.tick(1000)

        
if __name__ == "__main__":
    sound()
    pg.init()
    main()
    pg.quit()
    sys.exit()