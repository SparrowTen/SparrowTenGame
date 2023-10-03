import pygame
from settings import SETTINGS
from entities.move_object import MoveObject
from physics import Physics

class Player(MoveObject):
    def __init__(self, pos: pygame.Vector2):
        super().__init__()
        self.physics = Physics()
        
        self.pos = pos
        self.player_asset = pygame.image.load(SETTINGS.WORKDIR + '/assets/player_default.png')
        self.jump = True
        self.jump_height = 300
        
    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.jump:
                self.velocity_y = -300
        if keys[pygame.K_a]:
            self.velocity_x = -100
        if keys[pygame.K_d]:
            self.velocity_x = 100
            
        self.pos.x += self.velocity_x * dt
        self.pos.y += self.velocity_y * dt
        
        self.physics.apply_gravity(self, dt)
        self.physics.apply_friction(self, dt)
            
    def render(self, screen:pygame.Surface):
        screen.blit(self.player_asset, self.pos)
    
