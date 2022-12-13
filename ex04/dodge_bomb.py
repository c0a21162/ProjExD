import pygame as pg
import sys
import random

def check_bound(obj_rct,scr_rct):
    #第一引数：こうかとんrectまたは爆弾rect
    #第二引数：スクリーンrect
    yoko,tate = +1,+1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top <scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko,tate

#追加機能1：BGM
def sound():                                        
    pg.mixer.init(frequency = 44100)
    pg.mixer.music.load("../fig/なんでしょう？.mp3")
    pg.mixer.music.play(1)
    

def main():
    clock = pg.time.Clock()
    #練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1200,700))
    scrn_rct = scrn_sfc.get_rect()
    pg_bg_sfc = pg.image.load("../fig/pg_bg.jpg")
    pg_bg_rct = pg_bg_sfc.get_rect()
    
    #練習3
    tori_sfc = pg.image.load("../fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 600,350
    scrn_sfc.blit(tori_sfc,tori_rct)
    
    #練習5
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_rct.centery = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(bomb_sfc,bomb_rct)
    vx,vy = +1,+1

    #追加機能3：爆弾2個目
    bomb_sfc2 = pg.Surface((20,20))
    bomb_sfc2.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc2,(255,0,0),(10,10),10)
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = random.randint(0,scrn_rct.width)
    bomb_rct2.centery = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(bomb_sfc2,bomb_rct2)
    vx2,vy2 = +1,+1

    #練習2
    while True:
        scrn_sfc.blit(pg_bg_sfc,pg_bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dict = pg.key.get_pressed()
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct,scrn_rct) != (+1,+1):
            #どこかしらはみ出ていたら
            if key_dict[pg.K_UP]:
                tori_rct.centery += 1
            if key_dict[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dict[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dict[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc,tori_rct)

        #練習6
        #一つ目の爆弾
        bomb_rct.move_ip(vx,vy)
        yoko,tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        #二つ目の爆弾
        bomb_rct2.move_ip(vx2,vy2)
        yoko,tate = check_bound(bomb_rct2,scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        bomb_rct.move_ip(vx2,vy2)
        scrn_sfc.blit(bomb_sfc2,bomb_rct2)

        #練習8
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb_rct2):
            #追加機能2：Game Over
            pg.mixer.music.stop()
            tori_sfc = pg.image.load("../fig/8.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc,0,8.0)
            tori_rct = tori_sfc.get_rect()
            tori_rct.center = 600,350
            scrn_sfc.blit(tori_sfc,tori_rct)
            fonto = pg.font.Font(None,80)
            text = fonto.render("Game Over",True,"RED")
            scrn_sfc.blit(text,(400,200))
            pg.display.update()
            clock.tick(1)  
            return
        
        #issues#7の変更前を一応残してます
        # if tori_rct.colliderect(bomb_rct2):
        #     #追加機能2：Game Over
        #     tori_sfc = pg.image.load("../fig/8.png")
        #     tori_sfc = pg.transform.rotozoom(tori_sfc,0,8.0)
        #     tori_rct = tori_sfc.get_rect()
        #     tori_rct.center = 600,350
        #     scrn_sfc.blit(tori_sfc,tori_rct)
        #     fonto = pg.font.Font(None,80)
        #     text = fonto.render("Game Over",True,"RED")
        #     scrn_sfc.blit(text,(400,200))
        #     pg.display.update()
        #     clock.tick(1)  
        #     return

        pg.display.update()
        clock.tick(1000)  


if __name__ == "__main__":
    sound()
    pg.init()
    main()
    pg.quit()
    sys.exit()