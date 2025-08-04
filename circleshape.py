import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, CircleShape):
        r1 = self.radius
        r2 = CircleShape.radius

        distance = self.position.distance_to(CircleShape.position)

        if distance <= r1 + r2:
            return True
        else:
            return False

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)        

    def update(self, dt):
        # sub-classes must override
        pass