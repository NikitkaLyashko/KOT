import pygame
import pygame.rect

wind=pygame.display.set_mode([1000,1000])
pict_cat=pygame.image.load("pics/cat1.png")


wind.blit(pict_cat,[500,1000-pict_cat.get_height()])

a=pygame.Rect(500,1000-pict_cat.get_height(),pict_cat.get_width(),pict_cat.get_height())

pygame.draw.rect(wind,[200,100,0],a,3)


umbrella=pygame.image.load("pics/umbrella.png")

umbr_2=pygame.transform.scale(umbrella,[200,200])

wind.blit(umbr_2,a.topright)

umb=pygame.Rect(a.right,a.top,umbr_2.get_width(),umbr_2.get_height())









pygame.display.flip()



