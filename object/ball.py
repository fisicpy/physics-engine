# import modules
import pygame
import object.object


class Ball(object.object.AbstractObjectClass):
    def __init__(self, surface, coords=(100, 100), radius=50, color=(255, 131, 0)):
        self.coords = list(coords)
        self.size = radius
        self.color = color
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.coords[0], self.coords[1]), self.size)
