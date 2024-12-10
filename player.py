import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self): # the specifications for the player sprite
        forward = pygame.Vector2(0, 1).rotate(self.rotation) 
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): # the actual appearance of the player sprite drawn to screen
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # updates the rotation instance variable

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # basic vector (0, 1) with direction determined by the rotation angle (direction player is facing)
        self.position += forward * PLAYER_SPEED * dt # magnitude of the vector modified, based on our predetermined constant

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = 0.3

    def update(self, dt): # calls on the player methods "move", "rotate" and "shoot" when the assigned key is pressed
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()

