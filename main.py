import random
import pygame as pg  # call the pygame

pg.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))  # initialize new pygame window

clock = pg.time.Clock()

def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])

def draw_grid(positions):  # we're drawing our grid in the window (horizantal)
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pg.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))  # what *does mean?

    for row in range(GRID_HEIGHT):
        pg.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    for cal in range(GRID_WIDTH):
        pg.draw.line(screen, BLACK, (cal * TILE_SIZE, 0), (cal * TILE_SIZE, HEIGHT))  # don't understand "end_pos"

    pass

# writing main loop
def main():
    running = True
    playing = False

    positions = set()
    positions.add((10, 10))

    while running:
        clock.tick(FPS)  # this loop is max is 60 times per second

        for event in pg.event.get():  # quit the game
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:  # make a event with mouse click
                x, y = pg.mouse.get_pos()  # take a position from coorditation of the mouse
                col = x // TILE_SIZE  # we make a more useful coordination for us
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)  # if we find some positions, we remove him
                else:
                    positions.add(pos)  # if position not in... we make it

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    playing = not playing
                if event.key == pg.K_c:
                    playing = False  # what different with "not playing" like we used upper?
                if event.key == pg.K_g:
                    positions = gen(random.randrange(2, 5) * GRID_WIDTH)


        screen.fill(GREY)  # how I understand, we make a collor of screen diferent
        draw_grid(positions)
        pg.display.update()

    pg.quit()


if __name__ == '__main__': # how I understand, this running, when I start this py file
    main()