import random

import model,pygame
import view

# pygame.key.set_repeat(25)

free_type=pygame.event.custom_type()
pygame.time.set_timer(free_type,3000,0)

free_type_2=pygame.event.custom_type()
pygame.time.set_timer(free_type_2,3000,0)

def controller():
    event=pygame.event.get()

    for cobitie in event:

        if cobitie.type==free_type:

            random_bool=random.randint(int(False),int(True))
            model.ride_cloud_right=bool(random_bool)

            # model.ride_cloud_right=not model.ride_cloud_right
        if cobitie.type==free_type_2:
            model.water_drop_under_cloud_def()

        if cobitie.type ==pygame.KEYDOWN and cobitie.key==pygame.K_SPACE:
            # model.blue_rect.top=random.randint(300,900)
            # x=1000-model.blue_rect.top
            # model.blue_rect.height=x


            model.blue_rect.height=random.randint(300,900)
            model.blue_rect.bottom = 1000
            model.wave.bottom=model.blue_rect.top


        if cobitie.type == pygame.QUIT:
            exit()



        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_RIGHT:
            model.right()


        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_LEFT:
            model.left()






    model.show_rect=pygame.key.get_pressed()[pygame.K_TAB]