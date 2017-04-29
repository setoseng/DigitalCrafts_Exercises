import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

width = 510
height = 480
blue_color = (97, 159, 182)
change_dir_countdown = 120
x_dir = 0

class Monster():
    def __init__(self):
        self.monster_x = 1
        self.monster_y = 5
class Player():
    def __init__(self):
        self.player_x = 10
        self.player_y = 40
        self.speed_x = 0
        self.speed_y = 0
player = Player()
monster = Monster()
def setup():
    global background_image
    global player_image
    global monster_image
    global screen
    global clock

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    background_image = pygame.image.load("images/background.png")
    player_image = pygame.image.load("images/hero.png")
    monster_image = pygame.image.load("images/monster.png")

def redraw (collided=False, textsurface=None):
    screen.fill(blue_color)
    screen.blit(background_image,[0,0])

    screen.blit(player_image,[player.player_x,player.player_y])
    screen.blit(monster_image,[monster.monster_x,monster.monster_y])
    if collided and textsurface:
        screen.blit(textsurface,(250,250))
    pygame.display.update()
    clock.tick(60)

def collided (player, monster):
    if player.player_x + 32 < monster.monster_x:
        return False
    elif monster.monster_x + 32 < player.player_x:
        return False
    elif player.player_y + 32 < monster.monster_y:
        return False
    elif monster.monster_y + 32 < player.player_y:
        return False
    return True

setup()
redraw()
def main():
   
    # Game initialization
    aim_position = pygame.mouse.get_pos()
    change_dir_countdown = 120
    x_dir = 0
    stop_game = False
    moving = False
    last_event = None

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS',30)
    textsurface = myfont.render('Some Text',False,(0,0,0))

    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYDOWN:
                moving = True
                last_event = event

            elif event.type == pygame.KEYUP:
                moving = False

            if event.type == pygame.QUIT:
                stop_game = True
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        if moving and last_event:
            if last_event.key == KEY_DOWN:
                player.speed_y = 1
                if player.player_y>410:
                    pass
                else:
                    player.player_y += 2
            elif last_event.key == KEY_UP:
                player.speed_y = -1
                if player.player_y<30:
                    pass
                else:
                    player.player_y -= 2
            elif last_event.key == KEY_LEFT:
                player.speed_x = -1
                if player.player_x<30:
                    pass
                else:
                    player.player_x -= 2
            elif last_event.key == KEY_RIGHT:
                player.speed_x = 1 
                if player.player_x>450:
                    pass
                else:
                    player.player_x += 2

            # deactivate the cooresponding speeds
            # when an arrow key is released
            if last_event.key == KEY_DOWN:
                player.speed_y = 0
            elif last_event.key == KEY_UP:
                player.speed_y = 0
            elif last_event.key == KEY_LEFT:
                player.speed_x = 0
            elif last_event.key == KEY_RIGHT:
                player.speed_x = 0

        change_dir_countdown -= 1
        if change_dir_countdown < 1:
            change_dir_countdown = 120
            x_dir = random.randint(0,3)
        if x_dir == 0:
            monster.monster_x +=2
            if monster.monster_x> 500:
                monster.monster_x =0
        if x_dir == 1:       
            monster.monster_x -=2
            if monster.monster_x<0:
                monster.monster_x =500
        if x_dir == 2:
            monster.monster_y +=2
            if monster.monster_y>500:
                monster.monster_y = 0
        if x_dir == 3:
            monster.monster_y -=2
            if monster.monster_y<0: 
                monster.monster_y = 500   

        # Draw background

        # Game display
        redraw(collided(player, monster), textsurface)

    pygame.quit()
if __name__ == '__main__':
    main()
