# grasper code for kicks and giggles

import RoboPiLib3 as RPL
import setup3
import pygame


pygame.init()

white = (255,255,255); black = (0,0,0)
red = (255,0,0); green = (127, 232, 134)
blue = (102, 136, 214); pink = (232, 13, 119)
grey = (203, 206, 214)

display_width = 400
display_height = 400
screen = pygame.display.set_mode((display_width,display_height))
screen.fill(white)
clock = pygame.time.Clock()

done = False

pin = 0

open = False
close = False



def pos():
    open = False
    close = False
    if event.type == pygame.KEYDOWN:

        # what key are they pressing? move accordingly
        if event.key == pygame.K_ESCAPE:
            done=True
            return done
        elif event.key == pygame.K_j:
            close = True
        elif event.key == pygame.K_l:
            open = True
        else:
            return False, False


    return open, close


while not done:
    clock.tick(60)
    # determine where want to be
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        else: # did something other than close
            open, close = pos() # figure out the change

        screen.fill(grey)
        if open == True:
            pygame.draw.circle(screen, pink, (200, 200), 100, 0)
            RPL.servoWrite(pin,1000)
        elif close == True:
            pygame.draw.circle(screen, blue, (200, 200), 100, 0)
            RPL.servoWrite(pin,1700)
        else:
            pygame.draw.circle(screen, black, (200, 200), 100, 0)
            RPL.servoWrite(pin,0)



# Be IDLE friendly
    pygame.display.update()



#please work rectangle
pygame.quit()
