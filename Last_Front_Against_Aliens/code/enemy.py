import arcade

RADIUS = 50
class Enemy:

    def __init__(self, x, y, health, sprite):
        self.x = x
        self.y = y
        self.health = health
        self.sprite = sprite

    def spawn(self):
        arcade.draw_circle_filled(self.x, self.y, RADIUS, arcade.color.RED, 0, -1)

    def move(self, speed):
        if(self.x >= 0):
            self.x -= speed
