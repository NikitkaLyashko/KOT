import random

import pygame
pygame.init()



def water_drop_under_cloud_def():
    global  show_water_drop

    rect_kaplya.centerx=cloud_small.centerx
    rect_kaplya.centery=cloud_small.centery
    show_water_drop = True




show_rect=True

free_type=pygame.event.custom_type()
pygame.time.set_timer(free_type,3000,0)

razvorot_kota="111"
ride_cloud_right=True
show_water_drop=True


def right():
    global razvorot_kota
    if vedro.right<=1000:

        razvorot_kota = "mirror"
        vedro.right+=20
        mirror_pit_right()


def left():
    global razvorot_kota
    if vedro.left >= 0:

        razvorot_kota = "111"
        vedro.left-=20
        mirror_pit_left()


def mirror_pit_left():

    cot.left=vedro.right-45
    zont.right=cot.right+20
    plot_rect.centerx = cot.centerx

def mirror_pit_right():


    cot.right=vedro.left+45
    zont.left=cot.left-20
    plot_rect.centerx = cot.centerx


def height_wave():

    blue_rect.bottom = 1000
    wave.bottom = blue_rect.top
    plot_rect.bottom = wave.top + 10
    cot.bottom = plot_rect.top + 10
    zont.bottom = cot.top + 30
    vedro.bottom = cot.top + 45
def ride_cloud():
    global ride_cloud_right,show_water_drop,kapli

    rect_kaplya.bottom+=5

    if rect_kaplya.colliderect(zont) and show_water_drop==True:
        show_water_drop=False


    if rect_kaplya.colliderect(vedro) and show_water_drop==True:
        show_water_drop = False
        kapli+=1

    if rect_kaplya.bottom>=wave.top and show_water_drop==True:

        show_water_drop=False
        # rect_kaplya.centerx = cloud_small.centerx
        # rect_kaplya.centery = cloud_small.centery
        blue_rect.height+=10
        blue_rect.bottom = 1000
        wave.bottom = blue_rect.top
        plot_rect.bottom = wave.top + 10
        cot.bottom = plot_rect.top + 10
        zont.bottom = cot.top + 30
        vedro.bottom = cot.top + 45
        print(blue_rect.height)




    if ride_cloud_right==True:
        cloud_small.right+=5
        if cloud_small.right>=1000:
            ride_cloud_right=False
    else:
        cloud_small.left -= 5
        if cloud_small.left<=0:
            ride_cloud_right=True

cot=pygame.Rect(450, 850, 150, 150)
zont=pygame.Rect(cot.right - 80, 1, 100, 100)
vedro=pygame.Rect(cot.left -20, 1, 70, 70)
cloud_small=pygame.Rect(200,100,100,100)
wave=pygame.Rect(0,870,1000,30)
blue_rect=pygame.Rect(0,900,1000,100)
plot_rect=pygame.Rect(300,1,250,30)
text=pygame.font.SysFont("Arial",20)
kapli=0
mirror_pit_left()
height_wave()
rect_kaplya = pygame.Rect(400, 180, 25, 25)
rect_kaplya.centerx=cloud_small.centerx
