import arcade
import controls # controlul
import enemy
import player

# Constants for screen size, title, and movement speed
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Window"
MOVEMENT_SPEED = 5

# Deschid fereastra
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Setez culoare background
arcade.set_background_color(arcade.color.ASH_GREY)

# Creez Imagine
om_sprite = arcade.Sprite("../assets/Om1.jpg", scale= 0.2)
om_sprite.center_x = SCREEN_WIDTH // 2
om_sprite.center_y = SCREEN_HEIGHT // 2

# health and spirte not yet implemented
enemy = enemy.Enemy(SCREEN_WIDTH - enemy.RADIUS, 90, 0, 0)

def on_draw():
    arcade.start_render()

    # Pun imaginea pe ecran
    om_sprite.draw()
    enemy.spawn()

    
def update(delta_time):
    # Upgradez pozitia la fiecare interval
    player.player_movement(om_sprite, SCREEN_WIDTH, SCREEN_HEIGHT)
    enemy.move(MOVEMENT_SPEED / 1.5)
    #print(om_sprite.center_x, om_sprite.center_y, end = "\n")

def setup():
    # apelez functia la fiecare interval (masurat in secunde)
    arcade.schedule(update, 1/60)

    # Setez functiile de baza
    arcade.window_commands.get_window().on_draw = on_draw
    arcade.window_commands.get_window().on_key_press = controls.on_key_press
    arcade.window_commands.get_window().on_key_release = controls.on_key_release

    # Rulez programul
    arcade.run()

# Rulez programul doar daca a fost executat direct
if __name__ == "__main__":
    setup()