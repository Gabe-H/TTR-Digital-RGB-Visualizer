import pygame
import pygame.draw
import math
import csv
from effects import *

## SVG dimensions
DRAWING_WIDTH = 762 # unit height of svg file
DRAWING_HEIGHT = 508 # unit width of svg file

ASPECT_RATIO = DRAWING_WIDTH/DRAWING_HEIGHT

## Desired screen width
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = int(SCREEN_WIDTH / ASPECT_RATIO) # Maintain drawing aspect ratio

SCALE_FACTOR = SCREEN_WIDTH/DRAWING_WIDTH

TRAIN_WIDTH = 3 * SCALE_FACTOR
TRAIN_HEIGHT = 20 * SCALE_FACTOR
CITY_RADIUS = 5 * SCALE_FACTOR

## PyGame Configuration
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
screen.fill("black")

# Lists containing pygame elements
# (after they're read from csv's)
train_nodes: list[Node] = []
city_nodes: list[Node] = []


## Draw rotated rectangle
# Source - https://stackoverflow.com/a/73855696
# Posted by Tim Swena
# Retrieved 2026-06-20, License - CC BY-SA 4.0
def draw_rectangle(x, y, width, height, color, rotation=0.0):
    """Draw a rectangle, centered at x, y.

    Arguments:
      x (int/float):
        The x coordinate of the center of the shape.
      y (int/float):
        The y coordinate of the center of the shape.
      width (int/float):
        The width of the rectangle.
      height (int/float):
        The height of the rectangle.
      color (str):
        Name of the fill color, in HTML format.
    """
    points = []

    rotation *= -1 # Reverse rotation amount. Debugging found this necessary

    # The distance from the center of the rectangle to
    # one of the corners is the same for each corner.
    radius = math.sqrt((height / 2)**2 + (width / 2)**2)

    # Get the angle to one of the corners with respect
    # to the x-axis.
    angle = math.atan2(height / 2, width / 2)

    # Transform that angle to reach each corner of the rectangle.
    angles = [angle, -angle + math.pi, angle + math.pi, -angle]

    # Convert rotation from degrees to radians.
    rot_radians = (math.pi / 180) * rotation

    # Calculate the coordinates of each point.
    for angle in angles:
        y_offset = -1 * radius * math.sin(angle + rot_radians)
        x_offset = radius * math.cos(angle + rot_radians)
        points.append((x + x_offset, y + y_offset))

    return pygame.draw.polygon(screen, color, points)

def read_trains(filename):
    ## Read rectangle locations from CSV
    with open(filename) as csvfile:
        # rows = csv.reader(f)
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                # i = int(row['index'])
                x = float(row['center_x']) * SCREEN_WIDTH/DRAWING_WIDTH
                y = float(row['center_y']) * SCREEN_HEIGHT/DRAWING_HEIGHT
                r = float(row['rotation_degrees'])

            except TypeError:
                continue


            # trains.append(draw_rectangle(x, y, W, H, COLOR_OFF, r))
            train_nodes.append(Node(x, y, r))

def draw_trains():
    for node in train_nodes:
        x = node.x
        y = node.y
        c = node.color
        r = node.rot

        draw_rectangle(x, y, TRAIN_WIDTH, TRAIN_HEIGHT, c, r)

def read_cities(filename):
    ## Read circle (city) locations from CSV
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                x = float(row['center_x']) * SCREEN_WIDTH/DRAWING_WIDTH
                y = float(row['center_y']) * SCREEN_HEIGHT/DRAWING_HEIGHT
            except:
                continue

            city_nodes.append(Node(x, y))

def draw_cities():
    for node in city_nodes:
        x = node.x
        y = node.y

        pygame.draw.circle(screen, "red", (x, y), CITY_RADIUS)


if __name__ == "__main__":
    read_trains("rectangle_centers_rotations.csv")
    read_cities("circle_centers.csv")

    draw_cities()

    min_x = min(node.x for node in train_nodes)
    max_x = max(node.x for node in train_nodes)
    min_y = min(node.y for node in train_nodes)
    max_y = max(node.y for node in train_nodes)

    DIMS = (min_x, min_y, max_x, max_y)

    # u = (node.x - min_x) / (max_x - min_x)
    # v = (node.y - min_y) / (max_y - min_y)

    ## Main loop
    while running:
        # if (pygame.time.get_ticks() // 6000) % 2:
        #     wipe_right_to_left()
        # else:
        #     wipe_left_to_right()

        radial_pulse(train_nodes, DIMS)

        draw_trains()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

        clock.tick(30) # FPS limiter

    pygame.quit()