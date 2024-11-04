import arcade
import controls # controlez jucatorul
import enemy # clasa inamicului

# Constante
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

# arcade.View arata o stare specifica a jocului
# in acest caz afiseaza pe ecran trasaturile grafice
# ale primului nivel
class Level1(arcade.View):

    def __init__(self):
        super().__init__()

        # Culoare background
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)

        print("Start Level1")
        # Creez Imagine
        self.om_sprite = arcade.Sprite("../assets/Om1.jpg", scale= 0.2)
        self.om_sprite.center_x = SCREEN_WIDTH // 2
        self.om_sprite.center_y = SCREEN_HEIGHT // 2

        # Viata si Sprite (ultimii 2 parametrii) inca neimplementati
        self.enemy = enemy.Enemy(SCREEN_WIDTH - enemy.RADIUS, 90, 0, 0)

    def on_draw(self):
        arcade.start_render()

        # Pun imaginea pe ecran
        self.om_sprite.draw()
        self.enemy.spawn()

    def update(self, delta_time):
        # Upgradez pozitia la fiecare interval
        #player.player_movement(self.om_sprite, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.enemy.move(MOVEMENT_SPEED / 1.5)

    def on_key_press(self, key, modifiers):
        controls.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        controls.on_key_release(key, modifiers)


        


