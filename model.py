import random

import pygame
pygame.init()

cot=pygame.Rect(450, 850, 150, 150)
zont=pygame.Rect(cot.right - 80, 1, 100, 100)
vedro=pygame.Rect(cot.left -20, 1, 70, 70)
cloud_small=pygame.Rect(200,100,100,100)
wave=pygame.Rect(0,870,1000,30)
blue_rect=pygame.Rect(0,900,1000,100)
plot_rect=pygame.Rect(300,1,250,30)
# zont.bottom=cot.top+30
# vedro.bottom=cot.top+45

plot_rect.bottom = wave.top + 30
cot.bottom=plot_rect.top+10
cot.centerx=plot_rect.centerx
vedro.left=cot.left-20
zont.left = cot.right - 75
zont.bottom=cot.top+30
vedro.bottom=cot.top+45


rect_kaplya = pygame.Rect(400, 180, 25, 25)
rect_kaplya.centerx=cloud_small.centerx

def water_drop_under_cloud_def():

    rect_kaplya.centerx=cloud_small.centerx
    rect_kaplya.centery=cloud_small.centery

def height_wave():
    blue_rect.height = random.randint(300, 900)
    blue_rect.bottom = 1000
    wave.bottom = blue_rect.top
    plot_rect.bottom = wave.top + 10
    cot.bottom = plot_rect.top + 10
    cot.centerx = plot_rect.centerx
    vedro.left = cot.left - 20
    zont.left = cot.right - 75
    zont.bottom = cot.top + 30
    vedro.bottom = cot.top + 45



show_rect=True

free_type=pygame.event.custom_type()
pygame.time.set_timer(free_type,3000,0)

razvorot_kota="111"
ride_cloud_right=True
show_water_drop=True
def ride_cloud():
    global ride_cloud_right,show_water_drop

    rect_kaplya.bottom+=5

    if rect_kaplya.bottom==wave.top:
        show_water_drop=False

    if rect_kaplya.top>=wave.bottom:
        show_water_drop=True




    if ride_cloud_right==True:
        cloud_small.right+=5
        if cloud_small.right>=1000:
            ride_cloud_right=False
    else:
        cloud_small.left -= 5
        if cloud_small.left<=0:
            ride_cloud_right=True

def right():
    global razvorot_kota
    if vedro.right<=1000:
        cot.right+=5
        zont.right+=5
        vedro.right+=5
        mirror_pit_right()
        razvorot_kota = "mirror"


def left():
    global razvorot_kota
    if vedro.left >= 0:

        cot.left-=5
        zont.right-=5
        vedro.left-=5
        mirror_pit_left()
        razvorot_kota = "111"


def mirror_pit_right():

    cot.left=vedro.left-100
    zont.left=cot.right-170


def mirror_pit_left():

    cot.left=vedro.right-50
    zont.left=cot.right-75

