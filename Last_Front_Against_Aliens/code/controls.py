import arcade

MOVEMENT_SPEED = 5
dx = 0
dy = 0

def on_key_press(key, modifiers):
    global dx, dy
    if key == arcade.key.W:
        dy = MOVEMENT_SPEED
    elif key == arcade.key.S:
        dy = -MOVEMENT_SPEED
    elif key == arcade.key.A:
        dx = -MOVEMENT_SPEED
    elif key == arcade.key.D:
        dx = MOVEMENT_SPEED

def on_key_release(key, modifiers):
    global dx, dy
    if key == arcade.key.W or key == arcade.key.S:
        dy = 0
    elif key == arcade.key.A or key == arcade.key.D:
        dx = 0