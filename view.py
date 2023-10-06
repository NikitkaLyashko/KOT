import random

import pygame,model
import pygame.rect
pygame.init()
wind=pygame.display.set_mode([1000,1000])
text=pygame.font.SysFont("Arial",50)


pict_cat=pygame.image.load("pics/cat1.png")
umbrella=pygame.image.load("pics/umbrella.png")
bucket=pygame.image.load("pics/bucket.png")
cloud=pygame.image.load("pics/cloud.png")
water_drop=pygame.image.load("pics/water_drop.png")
water_wave=pygame.image.load("pics/water.png")
plot_pict=pygame.image.load("pics/raft.png")


cat_2 = pygame.transform.scale(pict_cat, [model.cot.width, model.cot.height])
umbr_2 = pygame.transform.scale(umbrella, [model.zont.width, model.zont.height])
bucket_2 = pygame.transform.scale(bucket, model.vedro.size)
cloud2=pygame.transform.scale(cloud,model.cloud_small.size)
water_drop_2=pygame.transform.scale(water_drop,[model.rect_kaplya.width,model.rect_kaplya.height])
wave_water_2=pygame.transform.scale(water_wave,model.wave.size)
plot_pict_2=pygame.transform.scale(plot_pict,model.plot_rect.size)



def textX(chislo):


    if chislo%10==0 or ( chislo%10>=5 and chislo%100<=19 ) or (chislo%100>=11 and chislo%100<=14) or (chislo%10>=5 and chislo%10<=9):
        text_kartinka = "ель"
        return text_kartinka

    if chislo%10==1 and chislo%100!=11:
        text_kartinka = "ля"
        return text_kartinka

    if chislo%10>1 and chislo%10 <5:
        text_kartinka = "ли"
        return text_kartinka






def mirror():
    kapl_do_yckor = " до ускорения"
    text_kartinka=textX(model.kapli)

    oconchanie_last_kaplya=textX(model.octaloc_kaplya)


    kartinka_2=text.render("кап"+text_kartinka+" "+str( model.kapli),True,[0, 150, 0])
    last_kaplya=text.render(str(model.octaloc_kaplya)+" кап"+oconchanie_last_kaplya+kapl_do_yckor,True,[0,150,0])

    level_text=text.render(str(model.level)+" уровень",True,[0,150,0])

    wind.fill([255, 125, 225])
    # pygame.draw.rect(wind, [90,124,56],model.c)
    wind.blit(cloud2, [model.cloud_small.left,model.cloud_small.top])
    if model.show_water_drop==True:
        wind.blit(water_drop_2,[model.rect_kaplya.left,model.rect_kaplya.top])

    wind.blit(wave_water_2, model.wave.topleft)
    wind.blit(plot_pict_2, model.plot_rect.topleft)

    wind.blit(level_text,[0,80])
    wind.blit(kartinka_2,[0,0])
    wind.blit(last_kaplya,[0,40])
    if model.razvorot_kota == "mirror":

        mirrior_cat_2=pygame.transform.flip(cat_2,True, False)
        wind.blit(mirrior_cat_2, [model.cot.left, model.cot.top])

        umbr_3=pygame.transform.flip(umbr_2,True,False)
        wind.blit(umbr_3,[model.zont.left, model.zont.top])

        bucket_3=pygame.transform.flip(bucket_2,True,False)
        wind.blit(bucket_3,model.vedro.topleft)
    else:

        wind.blit(cat_2, [model.cot.left, model.cot.top])
        wind.blit(umbr_2,[model.zont.left, model.zont.top])
        wind.blit(bucket_2, model.vedro.topleft)

    pygame.draw.rect(wind, [59, 163, 198], model.blue_rect)
    # wind.blit(wave_water_2, model.wave.topleft)









    rects()
    pygame.display.flip()

def rects():
    if model.show_rect==True:
        pygame.draw.rect(wind, [200, 100, 0], model.cot, 3)
        pygame.draw.rect(wind, [0, 200, 0], model.zont, 3)
        pygame.draw.rect(wind, [0, 0, 200], model.vedro, 3)
        pygame.draw.rect(wind,[0,0,0],model.cloud_small,3)
        pygame.draw.rect(wind,[100,200,150],model.rect_kaplya,3)
        pygame.draw.rect(wind,[0,0,0],model.wave,3)
        pygame.draw.rect(wind,[154,0,57],model.plot_rect,3)













pygame.display.flip()



