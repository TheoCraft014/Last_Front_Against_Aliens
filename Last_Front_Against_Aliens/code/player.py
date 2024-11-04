import arcade
import controls

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# mai e de lucru
def player_movement(player: arcade.Sprite, SCREEN_HEIGHT, SCREEN_WIDTH):
    if player.center_x > 0 and player.center_x < SCREEN_WIDTH:
        player.center_x += controls.dx
    elif player.center_x < 0:
        player.center_x += 20
    elif player.center_x > SCREEN_WIDTH:
        player.center_x -= 20

    if player.center_y > 0 and player.center_y < SCREEN_HEIGHT:
        player.center_y += controls.dy
    elif player.center_y < 0:
        player.center_y += 20
    elif player.center_y > SCREEN_HEIGHT:
        player.center_y -= 20

    
    