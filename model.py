import random

import pygame

cot=pygame.Rect(450, 800, 150, 150)
zont=pygame.Rect(cot.right - 80, 1, 100, 100)

vedro=pygame.Rect(cot.left -20, 1, 70, 70)
zont.bottom=cot.top+30
vedro.bottom=cot.top+45

show_rect=True

razvorot_kota="111"



def right():
    global razvorot_kota
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

