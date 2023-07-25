import model,pygame
import view

pygame.key.set_repeat(25)
def controller():
    event=pygame.event.get()

    for cobitie in event:

        if cobitie.type == pygame.QUIT:
            exit()



        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_RIGHT:
            model.right()
            model.mirror_pit_right()
            model.razvorot_kota = "mirror"

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_LEFT:
            model.left()
            model.mirror_pit_left()
            model.razvorot_kota="111"





    model.show_rect=pygame.key.get_pressed()[pygame.K_TAB]