import pygame

wind=pygame.display.set_mode([1000,1000])
pict_cat=pygame.image.load("pics/cat1.png")

wind.blit(pict_cat,[500,900])

pygame.display.flip()



