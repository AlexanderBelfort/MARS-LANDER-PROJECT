# Aleksandar T. Stefanov
# Mars Lander Alpha

import pygame
from pygame import *
from random import randint, random, uniform, choice
from math import sin, cos, radians
pygame.init()
from time import clock
mars_font = pygame.font.SysFont("monospace", 15)
mars_big = pygame.font.SysFont("Arial Black", 50)

FPS = 30
WIDTH = 1200
HEIGHT = 720
game_clock = pygame.time.Clock()

# we create our superclass
# that we will be needing
# quite often

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, left, top):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

# we create a thrust class
# needed to display the
# thrust in the engine

class Thrust(Sprite):
    def __init__(self, image_file, left, top):
        super().__init__(image_file,left, top)
        self.image_rotated = self.image

    def rotated(self):
        self.image_rotated = pygame.transform.rotate(self.image, rover.angle)


# we create our main class
# where we will add most
# of our properties
# and functions

class MarsRover(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed_y = random()
        self.speed_x = uniform(-1, 1)
        self.lives = 3
        self.rotated_image = self.image
        self.fuel = 500
        self.damage = 0
        self.angle = 0
        self.failure = randint(int(clock() + 5), int(clock() + 15))

    def mars_game_over(self):
        return self.lives < 1

    def Mars_Gravity(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.speed_y += 0.05     # this is the speed of the free fall

    def Start_Engine(self):
        self.speed_x += 0.33 * sin(radians(-self.angle))
        self.speed_y -= 0.33 * cos(radians(self.angle))
        self.fuel -= 5           # fuel will lose 5 any time space is pressed


    def reset_stats(self):       # we will need this function
        self.rect.top = 0        # any time game ends or restats
        self.speed_y = random()
        self.speed_x = uniform(-1, 1)
        self.rotated_image = self.image
        self.fuel = 500
        self.damage = 0
        self.angle = 0
        self.failure = self.control_block()

    def fixation(self):                 # we create a function
        if self.rect.bottom > HEIGHT:   # where if the lander should fall off the screen
            self.lives -= 1             # one life would be taken
            self.reset_stats()          # and if the lander should go to the left or right
            return True                 # side, he would come back at the screen
        if self.rect.left >= WIDTH:
            self.rect.left = 0
        if self.rect.right <= 0:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed_y = 0

    def move_left(self):
        self.angle += 1
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)

    def move_right(self):
        self.angle -= 1
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)

    # we will need a few landing functions
    # so that the lander falls right
    # and does not break any laws of physics


    def landing_condition(self):
        return self.fuel > 0 and self.damage < 100

    def landing_correct(self):
        return -5 < self.angle < 5

    def check_landing_speed(self):
        return -5 < self.speed_x < 5 and self.speed_y < 5

    def control_block(self):
        return randint(int(clock() + 5), int(clock() + 15))

# we create a class
# for our meteors so that
# they can free fall like our rover

class Meteor(Sprite):
    def __init__(self, image_file, left, top):
        super().__init__(image_file, left, top)

        self.speed_y = random()
        self.speed_x = uniform(-1, 1)

    def meteor_free_fall(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.speed_y += 0.02


# we import our main sources
# our rover
# pads, obstacles
# and meteors

screen = pygame.display.set_mode((1200,750))
rover = MarsRover("lander.png", [randint(0, 1120), 0])
game_pads = pygame.sprite.Group()
pad1 = Sprite('pad.png', randint(0, 200), 720).add(game_pads)
pad2 = Sprite('pad.png', randint(440, 700), 620).add(game_pads)
pad3 = Sprite('pad_tall.png', randint(900, 1000), 650).add(game_pads)
test = Sprite('mars_background_instr.png', 0,0)
pygame.display.set_caption("MARS LANDER ALPHA")

obstacles = pygame.sprite.Group()
obstacles1 = Sprite('building_dome.png', 20, 530).add(obstacles)
obstacles2 = Sprite('building_station_SW.png', 350, 650).add(obstacles)
obstacles3 = Sprite('pipe_stand_SE.png', 797, 630).add(obstacles)
obstacles4 = Sprite('rocks_ore_SW.png', 177, 450).add(obstacles)
obstacles5 = Sprite('satellite_SW.png', 1100, 399).add(obstacles)
obstacle6 = Sprite('pipe_ramp_NE.png', 100, 170).add(obstacles)

meteors = pygame.sprite.Group()
meteor1 = Meteor('spaceMeteors_001.png', randint(0, 100), 100).add(meteors)
meteor2 = Meteor('spaceMeteors_004.png', randint(0, 100), 300).add(meteors)
meteor3 = Meteor('spaceMeteors_003.png', randint(0, 100), 150).add(meteors)
meteor4 = Meteor('spaceMeteors_004.png', randint(666, 777), 500).add(meteors)
meteor5 = Meteor('spaceMeteors_003.png', randint(666, 777), 50).add(meteors)
meteor6 = Meteor('spaceMeteors_001.png', randint(666, 777), 666).add(meteors)
meteor7 = Meteor('spaceMeteors_001.png', randint(666, 777), 100).add(meteors)
game_score = 0

# storm initializer
# we will call this every time
# a game is won or
# a game is lost
# so that random storms would appear

def stormi():
    stormy = randint(int(clock())+5, int(clock())+12)
    return stormy

storm = stormi()

# crash initializer with message

def crash():
    global storm
    crashed = mars_big.render('You Have Crashed', False, (255, 0, 0))
    while True:
        screen.blit(crashed, (340, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                storm = stormi()
                return
            if event.type == KEYDOWN:
                storm = stormi()
                return
        pygame.display.update()

# win initalizer with message

def win():
    global storm
    won = mars_big.render('You WON!', False, (255, 0, 0))
    while True:
        screen.blit(won, (340, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                storm = stormi()
                return
            if event.type == KEYDOWN:
                storm = stormi()
                return
        pygame.display.update()

# we create our game initalizer

def game(score):

    block_key = choice((pygame.K_SPACE, pygame.K_LEFT, pygame.K_RIGHT))
    while not rover.mars_game_over():
        keys_pressed = pygame.key.get_pressed()
        game_clock.tick(FPS)
        screen.fill([255, 255, 255])
        screen.blit(test.image, test.rect)
        game_pads.draw(screen)
        obstacles.draw(screen)

        my_clock = pygame.time.get_ticks() / 1000 # convert to seconds

        # we invent our scoreboard
        # using properties
        # of our main class

        my_time = mars_font.render(' {:.1f}'.format(my_clock), False, (255, 255, 255))
        my_fuel = mars_font.render(" {}".format(rover.fuel), False, (255, 255, 255))
        my_damage = mars_font.render(str(rover.damage), False, (255, 255, 255))
        my_alt = mars_font.render("{:.1f}".format(1000*(1-(rover.rect.top/HEIGHT))), False, (255, 255, 255))
        x_velo = mars_font.render("{:.1f}".format(rover.speed_x), False, (255, 255, 255))
        y_velo = mars_font.render("{:.1f}".format(rover.speed_y), False, (255, 255, 255))
        my_score = mars_font.render("{}".format(score), False, (255, 255, 0))
        my_lives = mars_font.render("LIVES: {}".format(rover.lives), False, (255, 255, 0))

        screen.blit(my_time, (74, 12))
        screen.blit(my_fuel, (74, 32))
        screen.blit(my_damage, (100, 57))
        screen.blit(my_alt, (269, 14))
        screen.blit(x_velo, (310, 37))
        screen.blit(y_velo, (310, 60))
        screen.blit(my_score, (74, 85))
        screen.blit(my_lives, (165, 85))

        screen.blit(rover.rotated_image, rover.rect)

        if clock() > storm:
            meteors.draw(screen)
            for meteor in meteors:        # we iterate through our meteors do we can add all of them
                meteor.meteor_free_fall() # we give them the same free fall our rover has

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                stormi()
                return
        obstacle_collision = pygame.sprite.spritecollide(rover, obstacles, True)  # any time rover collides with obstacle
        if obstacle_collision:                                                    # we make the obstacle dissapear
                rover.damage += 10                                                # and we damage the rover

        meteor_collision = pygame.sprite.spritecollide(rover, meteors, True)      # collision with meteors
        if meteor_collision:                                                      # will cost us more
                rover.damage +=25

        landing_pad_collision = pygame.sprite.spritecollideany(rover, game_pads)
        if landing_pad_collision:
            # we create an if statement that will want our rover
            # to land correctly inside the pad with appropriate speed
            # and executing a correct landing will give us points
            # but if failure to land we will lose 1 life and crash
            if rover.landing_condition() and rover.rect.left > landing_pad_collision.rect.left and rover.rect.right \
                    <= landing_pad_collision.rect.right and rover.check_landing_speed() and rover.landing_correct():
                score += 50
                block_key = choice((pygame.K_SPACE, pygame.K_LEFT, pygame.K_RIGHT))
                rover.reset_stats()
                win()
            else:
                block_key = choice((pygame.K_SPACE, pygame.K_LEFT, pygame.K_RIGHT))
                rover.lives -= 1
                rover.reset_stats()
                crash()
            # we use win() and crash() to also initalize our win and crash pop-ups

        if not rover.failure < clock() < rover.failure + 2:
                                                   # we create an if statement
            if keys_pressed[pygame.K_LEFT]:        # where our rover will only operate
                rover.move_left()                  # if it has fuel and is not fully damaged
            if keys_pressed[pygame.K_RIGHT]:
                rover.move_right()
            if keys_pressed[pygame.K_SPACE]:
                thrust = Thrust('thrust.png', rover.rect.left + 31, rover.rect.bottom - 12)
                thrust.rotated()
                rover.Start_Engine()
                screen.blit(thrust.image_rotated, thrust.rect)
        else:
            alert_control = mars_big.render('ALERT!!', False, (0, 0, 255))
            screen.blit(alert_control, (240, 90))
            if block_key == pygame.K_RIGHT:
                if keys_pressed[pygame.K_LEFT]:  # where our rover will only operate
                    rover.move_left()  # if it has fuel and is not fully damaged
                if keys_pressed[pygame.K_SPACE]:
                    thrust = Thrust('thrust.png', rover.rect.left + 31, rover.rect.bottom - 12)
                    thrust.rotated()
                    rover.Start_Engine()
                    screen.blit(thrust.image_rotated, thrust.rect)
            elif block_key == pygame.K_LEFT:
                if keys_pressed[pygame.K_RIGHT]:
                    rover.move_right()
                if keys_pressed[pygame.K_SPACE]:
                    thrust = Thrust('thrust.png', rover.rect.left + 31, rover.rect.bottom - 12)
                    thrust.rotated()
                    rover.Start_Engine()
                    screen.blit(thrust.image_rotated, thrust.rect)
            else:
                if keys_pressed[pygame.K_LEFT]:  # where our rover will only operate
                    rover.move_left()  # if it has fuel and is not fully damaged
                if keys_pressed[pygame.K_RIGHT]:
                    rover.move_right()
        screen.blit(rover.rotated_image, rover.rect)

        pygame.display.update()

        rover.Mars_Gravity()
        if rover.fixation():
            crash()
        pygame.display.flip()

    pygame.quit()

game(game_score)