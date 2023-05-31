import pygame
import random

'''from dino_runner.components import power_ups'''
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, HAMMER_TYPE, SHIELD_TYPE
from dino_runner.utils.constants import SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS, BIRD_Y_POS
from dino_runner.utils.constants import SCREEN_WIDTH
'''from dino_runner.components.power_ups import power_up, power_up_manager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield'''


class ObstacleManager():
    

    def __init__(self):
        self.obstacles = []
        self.obst = 0
        
    def update(self, game):
       
        if len(self.obstacles) == 0:
            obst = random.randint(1,3)
            self.obst = obst
            if obst == 1:
                obstacle = Cactus(SMALL_CACTUS)
            elif obst == 2:
                obstacle = Cactus(LARGE_CACTUS)
            else:
                obstacle = Bird(BIRD) 

            self.obstacles.append(obstacle)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
               if (game.player.type == SHIELD_TYPE and not self.obst == 3) or (game.player.type == HAMMER_TYPE and self.obst == 3)  or not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
               else:
                    self.obstacles.remove(obstacle)
        
            
        
        
   
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()