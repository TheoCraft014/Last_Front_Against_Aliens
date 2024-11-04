import arcade
import menu
import Level1

# Constante
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Last Front: Against Aliens"

def main():

    # Creez fereastra
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Instantiez primul nivel si il rulez pe fereastra
    level1 = Level1.Level1()
    window.show_view(level1)

    # Rulez programul
    arcade.run()

# Rulez programul doar daca a fost executat direct
if __name__ == "__main__":
    main()