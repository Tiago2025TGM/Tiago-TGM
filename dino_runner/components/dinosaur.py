import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, JUMP_SOM, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinosaur:

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.jump_sound_playing = False
        self.dino_duck = False

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 35
        self.step_index	+= 1

        if self.step_index >= 10:
            self.step_index = 0

    '''def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.dino_jump:
            self.dino_run = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        else:                                 
            self.jump_sound_playing = False   

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()'''
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
            
        if user_input[pygame.K_UP]:          
            if not self.jump_sound_playing:   ##
                JUMP_SOM.play()              ##
                self.jump_sound_playing = True  ##
            if user_input[pygame.K_UP] and not self.dino_jump:
                self.dino_run = False
                self.dino_jump = True
                self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        else:                                 ##
            self.jump_sound_playing = False      
       
        if self.step_index >= 9:
            self.step_index = 0
        
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))