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
