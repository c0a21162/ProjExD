import pygame as pg
import sys

def main():
    #ここにゲームの処理を書く予定
    clock = pg.time.Clock()

    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((800,600))

    tori_sfc = pg.image.load("../fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,90,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 400,300
    scrn_sfc.blit(tori_sfc,tori_rct)

    pg.display.update()
    clock.tick(0.2)

    # while True:
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             return

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()