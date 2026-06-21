import pygame
import pygame.draw
import math
import csv
from effects import *
from board import *

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
                # Get geometric data
                x = float(row['center_x']) * SCREEN_WIDTH/DRAWING_WIDTH
                y = float(row['center_y']) * SCREEN_HEIGHT/DRAWING_HEIGHT
                r = float(row['rotation_degrees'])

                # Add to list for display
                node = Node(x, y, r)
                train_nodes.append(Node(x, y, r))

                # Get id data
                label = row['label']
                label_parts = list(map(int, label.split('-')))

                connection_id = label_parts[0]
                node_index = label_parts[1]

                try:
                    track_index = label_parts[2]
                except IndexError:
                    track_index = 0

                connections[connection_id].set_node(node, node_index-1, track_index-1)

            except TypeError:
                continue


def draw_trains():
    for node in train_nodes:
        x = node.x
        y = node.y
        c = node.color
        r = node.rot

        if c is None:
            c = COLOR_OFF

        draw_rectangle(x, y, TRAIN_WIDTH, TRAIN_HEIGHT, c, r)

def read_cities(filename):
    ## Read circle (city) locations from CSV
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                x = float(row['center_x']) * SCREEN_WIDTH/DRAWING_WIDTH
                y = float(row['center_y']) * SCREEN_HEIGHT/DRAWING_HEIGHT
                label = row['label']

                node = Node(x, y)
                city_nodes.append(node)

                found = False
                for city in cities:
                    if city.name == label:
                        found = True
                        city.add_node(node)

                if not found:
                    print("failed to find", label)

            except:
                print("failed to parse row: ", row)

def draw_cities():
    for node in city_nodes:
        x = node.x
        y = node.y
        c = node.color

        if c is None:
            c = COLOR_OFF

        pygame.draw.circle(screen, c, (x, y), CITY_RADIUS)


def load_relative_coords(nodes: list[Node], min_x, max_x, min_y, max_y):
    for i in range(len(nodes)):
        u = (nodes[i].x - min_x) / (max_x - min_x)
        v = (nodes[i].y - min_y) / (max_y - min_y)

        nodes[i].set_relative_position(u, v)


if __name__ == "__main__":
    read_trains("rectangle_centers_rotations.csv")
    read_cities("circle_centers.csv")

    draw_cities()

    min_x = min(node.x for node in train_nodes)
    max_x = max(node.x for node in train_nodes)
    min_y = min(node.y for node in train_nodes)
    max_y = max(node.y for node in train_nodes)

    DIMS = (min_x, min_y, max_x, max_y)

    load_relative_coords(train_nodes, min_x, max_x, min_y, max_y)
    load_relative_coords(city_nodes, min_x, max_x, min_y, max_y)

    effect_index = 0
    ## Main loop
    while running:
        effect_index = (pygame.time.get_ticks() // 5000) % 3
        screen.fill('black')

        # if effect_index == 0:
            # wipe_right_to_left(train_nodes)
        # elif effect_index == 1:
            # wipe_left_to_right(train_nodes)
        # elif effect_index == 2:
            # radial_pulse(train_nodes)

        # wipe_right_to_left(train_nodes)
        # wipe_left_to_right(train_nodes)
        # radial_pulse(train_nodes)
        spinner(train_nodes)
        # spinner(city_nodes)

        draw_trains()
        draw_cities()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

        clock.tick(50) # FPS limiter

    pygame.quit()