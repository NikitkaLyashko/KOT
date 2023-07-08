import pygame,model
import pygame.rect

wind=pygame.display.set_mode([1000,1000])



pict_cat=pygame.image.load("pics/cat1.png")
pygame.draw.rect(wind, [200,100,0], model.cot, 3)
cat_2=pygame.transform.scale(pict_cat, [model.cot.width, model.cot.height])
wind.blit(cat_2, [model.cot.left, model.cot.top])


pygame.draw.rect(wind, [0,200,0], model.zont, 3)
umbrella=pygame.image.load("pics/umbrella.png")
umbr_2=pygame.transform.scale(umbrella, [model.zont.width, model.zont.height])
wind.blit(umbr_2, [model.zont.left, model.zont.top])

pygame.draw.rect(wind, [0,0,200], model.vedro, 3)
bucket=pygame.image.load("pics/bucket.png")
bucket_2=pygame.transform.scale(bucket, model.vedro.size)
wind.blit(bucket_2, model.vedro.topleft)

















pygame.display.flip()



