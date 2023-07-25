import pygame,model
import pygame.rect
pygame.init()
wind=pygame.display.set_mode([1000,1000])



pict_cat=pygame.image.load("pics/cat1.png")
umbrella=pygame.image.load("pics/umbrella.png")
bucket=pygame.image.load("pics/bucket.png")

cat_2 = pygame.transform.scale(pict_cat, [model.cot.width, model.cot.height])
umbr_2 = pygame.transform.scale(umbrella, [model.zont.width, model.zont.height])
bucket_2 = pygame.transform.scale(bucket, model.vedro.size)

def mirror():
    wind.fill([255, 125, 225])

    if model.razvorot_kota == "mirror":



        mirrior_cat_2=pygame.transform.flip(cat_2,True, False)
        wind.blit(mirrior_cat_2, [model.cot.left, model.cot.top])

        umbr_3=pygame.transform.flip(umbr_2,True,False)
        wind.blit(umbr_3,[model.zont.left, model.zont.top])

        bucket_3=pygame.transform.flip(bucket_2,True,False)
        wind.blit(bucket_3,model.vedro.topleft)
    else:

        wind.blit(cat_2, [model.cot.left, model.cot.top])
        wind.blit(umbr_2,[model.zont.left, model.zont.top])

        wind.blit(bucket_2, model.vedro.topleft)










    rects()
    pygame.display.flip()

def rects():
    if model.show_rect==True:
        pygame.draw.rect(wind, [200, 100, 0], model.cot, 3)
        pygame.draw.rect(wind, [0, 200, 0], model.zont, 3)
        pygame.draw.rect(wind, [0, 0, 200], model.vedro, 3)









pygame.display.flip()



