import pygame
import random
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def main():
    width = 510
    height = 480
    blue_color = (97, 159, 182)
    change_dir_countdown = 120
    x_dir = 0

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    background_image = pygame.image.load("images/background.png")
    player_image = pygame.image.load("images/hero.png")
    monster_image = pygame.image.load("images/monster.png")
    # Game initialization
    aim_position = pygame.mouse.get_pos()
    player_x = 20
    player_y = 40
    monster_x = 20
    monster_y = 15
    change_dir_countdown = 120

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    player_y += 10
                elif event.key == KEY_UP:
                    player_y -= 10
                elif event.key == KEY_LEFT:
                    player_x -= 10
                elif event.key == KEY_RIGHT:
                    player_x += 10
            if event.type == pygame.QUIT:
                stop_game = True
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        change_dir_countdown -= 1
        if change_dir_countdown < 1:
            change_dir_countdown = 120
            x_dir = random.randint(0,3)
        if x_dir == 0:
            monster_x +=2
            if monster_x> 500:
                monster_x =0
        if x_dir == 1:       
            monster_x -=2
            if monster_x<0:
                monster_x =0
        if x_dir == 2:
            monster_y +=2
            if monster_y>500:
                monster_y = 0
        if x_dir == 3:
            monster_y -=2
            if monster_y<0: 
                monster_y = 500   
        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image,[0,0])

        # Game display
        screen.blit(player_image,[player_x,player_y])
        screen.blit(monster_image,[monster_x,monster_y])
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
