import pygame as pg  # call the pygame

pg.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIDE = 20
GRID_WIDTH = WIDTH // TILE_SIDE
GRID_GEIGHT = HEIGHT // TILE_SIDE
FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))  # initialize new pygame window

clock = pg.time.Clock()

# writing main loop (what?)
def main():
    running = True
    while running:
        clock.tick(FPS)  # this loop is max is 60 times per second

        for event in pg.event.get():  # quit the game
            if event.type == pg.QUIT:
                running = False

    pg.quit()


if __name__ == '__main__': # how I understand, this running, when I start this py file
    main()