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
    cot.right+=5
    zont.right+=5
    vedro.right+=5


def left():
    if vedro.left >= 0:

        cot.left-=5
        zont.right-=5
        vedro.left-=5


def mirror_pit_right():
    global zont,vedro

    zont = pygame.Rect(cot.right - 170, 1, 100, 100)
    vedro = pygame.Rect(cot.left + 100, 1, 70, 70)
    zont.bottom = cot.top + 30
    vedro.bottom = cot.top + 45

def mirror_pit_left():
    global zont,vedro
    zont = pygame.Rect(cot.left +70, 1, 100, 100)
    vedro = pygame.Rect(cot.right - 170, 1, 70, 70)
    zont.bottom = cot.top + 30
    vedro.bottom = cot.top + 45