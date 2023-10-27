import random

import model,pygame
import view

pygame.key.set_repeat(25)

free_type=pygame.event.custom_type()

pygame.time.set_timer(free_type,3000,0)



def controller():

    event=pygame.event.get()


    for cobitie in event:

        if cobitie.type==free_type:
            random_bool=random.randint(int(False),int(True))
            model.ride_cloud_right=bool(random_bool)

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_RETURN:

            model.cloud_controller()


        if cobitie.type == model.free_type_dlya_sun:
            model.show_sun = False

        if cobitie.type==model.free_type_2:
            model.water_drop_under_cloud_def()

        if cobitie.type ==pygame.KEYDOWN and cobitie.key==pygame.K_SPACE:
            model.kapli+=1

        if cobitie.type == pygame.QUIT:
            exit()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_d:
            model.right()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_a:
            model.left()

    model.show_rect=pygame.key.get_pressed()[pygame.K_TAB]