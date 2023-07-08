import random

import pygame

cot=pygame.Rect(450, 800, 150, 150)
zont=pygame.Rect(cot.right - 80, 1, 100, 100)
vedro=pygame.Rect(cot.left -20, 1, 70, 70)
zont.bottom=cot.top+30
vedro.bottom=cot.top+45

def probel():
    x=random.randint(0,1000)
    cot.width=x

