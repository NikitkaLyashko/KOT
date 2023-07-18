import random

import pygame

cot=pygame.Rect(450, 800, 150, 150)
zont=pygame.Rect(cot.right - 80, 1, 100, 100)
vedro=pygame.Rect(cot.left -20, 1, 70, 70)
zont.bottom=cot.top+30
vedro.bottom=cot.top+45

show_rect=True

razvorot_kota="mirror_2"

def probel():
    x=random.randint(0,1000)
    cot.left=x
    zont.left=x
    vedro.left=x
    zont.left = cot.right - 80
    vedro.left = cot.left -20

def right():
    cot.right+=5
    zont.right+=5
    vedro.right+=5


def left():
    if vedro.left >= 0:
        cot.left-=5
        zont.right-=5
        vedro.left-=5



