import random

import pygame
pygame.init()

cot=pygame.Rect(450, 800, 150, 150)
zont=pygame.Rect(cot.right - 80, 1, 100, 100)
vedro=pygame.Rect(cot.left -20, 1, 70, 70)
cloud_small=pygame.Rect(200,100,100,100)

zont.bottom=cot.top+30
vedro.bottom=cot.top+45

show_rect=True

free_type=pygame.event.custom_type()
pygame.time.set_timer(free_type,3000,0)

razvorot_kota="111"
ride_cloud_right=False
def ride_cloud():
    global ride_cloud_right





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

