import pygame
import random
import time

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 800
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT
BACKGROUND = [36, 188, 168]
FOOD_COLOUR = [220,20,60]
SNAKE_COLOUR = [255,255,0]

pygame.init()
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
screen.fill(BACKGROUND)
pygame.display.update()

def final_score(length):
    screen.fill(BACKGROUND)
    font = pygame.font.Font(None, 40)
    text = font.render(f"YOUR SCORE WAS: {length - 1}", True, (0, 0, 0))
    screen.blit(text,(WINDOW_WIDTH/3,WINDOW_HEIGHT/2))
    pygame.display.update()

def play_game():
    x = screen.get_width() / 2
    y = screen.get_height() / 2
    radius = 10
    diameter = 2 * radius
    length = 1
    circle_centers = [[x, y]]
    velocity = [[diameter, 0]]
    food_coords = [random.randint(0,screen.get_width()-2*radius),random.randint(0,screen.get_height()-2*radius)]
    while True:
        if abs(circle_centers[0][0]-food_coords[0])<=diameter and abs(circle_centers[0][1]-food_coords[1])<=diameter:
            velocity.append(velocity[length - 1])
            food_coords =  [random.randint(0,screen.get_width()-2*radius),random.randint(0,screen.get_height()-2*radius)]
            circle_centers.append([circle_centers[length-1][0]-velocity[length-1][0],circle_centers[length-1][1]-velocity[length-1][1]])
            length += 1
            #IF SNAKE GETS FOOD, WE ADD IT TO THE BODY

        for i in range(1, length):
            velocity[length - i] = velocity[length - i - 1] #UPDATING VELOCITIES FOR MOVEMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if length > 1:
                        if velocity[1][1] <= 0:
                            velocity[0] = [0, -2 * radius]
                    else: velocity[0] = [0, -2 * radius]

                if event.key == pygame.K_DOWN:
                    if length>1:
                        if velocity[1][1] >= 0:
                            velocity[0] = [0, 2 * radius]
                    else: velocity[0] = [0, 2 * radius]

                if event.key == pygame.K_LEFT:
                    if length>1:
                        if velocity[1][0] <= 0:
                            velocity[0] = [-2 * radius, 0]
                    else: velocity[0] = [-2 * radius, 0]

                if event.key == pygame.K_RIGHT:
                    if length>1:
                        if velocity[1][0] >= 0:
                            velocity[0] = [2 * radius, 0]
                    else: velocity[0] = [2 * radius, 0]

        for i in range(0, length):
            circle_centers[i][0] += velocity[i][0]
            circle_centers[i][1] += velocity[i][1]
        if circle_centers[0][0] - radius < 0 or circle_centers[0][0] + radius > screen.get_width():
            final_score(length)
            time.sleep(4)
            return

        if circle_centers[0][1] - radius < 0 or circle_centers[0][1] + radius > screen.get_height():
            final_score(length)
            time.sleep(4)
            return

        for i in range(1,length):
            if circle_centers[0] == circle_centers[i]:
                final_score(length)
                time.sleep(4)
                return


        screen.fill(BACKGROUND)
        pygame.draw.circle(screen,FOOD_COLOUR,food_coords,radius)
        font = pygame.font.Font(None, 40)
        text = font.render(f"SCORE : {length-1}", True, (0, 0, 0))
        screen.blit(text, (20, 20))
        for i in range(0, length):
            pygame.draw.circle(screen, SNAKE_COLOUR, (circle_centers[i][0], circle_centers[i][1]), radius)

        pygame.display.update()
        clock.tick(10)


play_game()