import pygame
import math

COLOR_OFF = (30, 30, 30)
COLOR_ON = (255, 255, 255)

class Node:
    def __init__(self, center_x, center_y, rot_deg=None, color=None):
        self.x = center_x
        self.y = center_y
        self.rot = rot_deg
        self.color = color

def wipe_right_to_left(nodes: list[Node], dims, bar_time=3, bar_width=0.1):
    """
    nodes: list of nodes to apply effect to
    dims: screen dimensions, tuple: (min_x, min_y, max_x, max_y)
    bar_time: time in seconds of loop
    bar_width: width as percentage of screen width (0.0-1.0)
    """
    t = pygame.time.get_ticks() / 1000.0 # Get current runtime in seconds
    bar_x = t % bar_time / bar_time # bt: "bar time"

    for node in nodes:
        u = (node.x - dims[0]) / (dims[2] - dims[0])
        # v = (node.y - dims[1]) / (dims[3] - dims[1])

        distance = abs(u - bar_x) # Distance from bar to node
        wrap_distance = abs(u - (bar_x - 1.0))

        if (distance < bar_width) or (wrap_distance < bar_width):
            node.color = COLOR_ON
        else:
            node.color = COLOR_OFF

def wipe_left_to_right(nodes: list[Node], dims: tuple, bar_time=3, bar_width=0.1):
    """
    nodes: list of nodes to apply effect to
    dims: screen dimensions, tuple: (min_x, min_yy, max_x, max_y)
    bar_time: time in seconds of loop
    bar_width: width as percentage of screen width (0.0-1.0)
    """

    t = pygame.time.get_ticks() / 1000.0 # Get current runtime in seconds
    bar_x = 1.0 - (t % bar_time / bar_time) # bt: "bar time"

    for node in nodes:
        u = (node.x - dims[0]) / (dims[2] - dims[0])
        # v = (node.y - dims[1]) / (dims[3] - dims[1])

        distance = abs(u - bar_x) # Distance from bar to node
        wrap_distance = abs(u - (bar_x - 1.0))

        if (distance < bar_width) or (wrap_distance < bar_width):
            node.color = COLOR_ON
        else:
            node.color = COLOR_OFF

def radial_pulse(nodes: list[Node], dims: tuple, pulse_time=2.0, pulse_width=0.1):
    t = pygame.time.get_ticks() / 1000.0 # Get current runtime in seconds

    pulse_radius = t % pulse_time / pulse_time

    for node in nodes:
        u = (node.x - dims[0]) / (dims[2] - dims[0])
        v = (node.y - dims[1]) / (dims[3] - dims[1])
        
        node_radius = math.sqrt((u - 0.5)**2 + (v - 0.5)**2)

        distance = abs(node_radius - pulse_radius)

        if (distance < pulse_width):
            # draw_rectangle(node.x, node.y, TRAIN_WIDTH, TRAIN_HEIGHT, COLOR_ON, node.rot)
            node.color = COLOR_ON
        else:
            # draw_rectangle(node.x, node.y, TRAIN_WIDTH, TRAIN_HEIGHT, COLOR_OFF, node.rot)
            node.color = COLOR_OFF