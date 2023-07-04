import pygame
import pygame.rect

wind=pygame.display.set_mode([1000,1000])
a=pygame.Rect(450,800,150,150)
b=pygame.Rect(a.right,a.top-100,100,100)
b.bottom=a.top


pict_cat=pygame.image.load("pics/cat1.png")
pygame.draw.rect(wind,[200,100,0],a,3)
cat_2=pygame.transform.scale(pict_cat,[a.width,a.height])
wind.blit(cat_2,[a.left,a.top])


pygame.draw.rect(wind,[0,200,0],b,3)
umbrella=pygame.image.load("pics/umbrella.png")
umbr_2=pygame.transform.scale(umbrella,[b.width,b.height])
wind.blit(umbr_2,[b.left,b.top])










#
# b=pygame.Rect(500,)
#
# umbrella=pygame.image.load("pics/umbrella.png")
#
# umbr_2=pygame.transform.scale(umbrella,[200,200])
#
# wind.blit(umbr_2,a.topright)
#
# # umb=pygame.Rect(a.right,a.top,umbr_2.get_width(),umbr_2.get_height())









pygame.display.flip()



