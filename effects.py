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

        self.u = None
        self.v = None


    def set_relative_position(self, u: float, v: float):
        self.u = u
        self.v = v

def wipe_right_to_left(nodes: list[Node], bar_time=3, bar_width=0.1):
    """
    nodes: list of nodes to apply effect to
    dims: screen dimensions, tuple: (min_x, min_y, max_x, max_y)
    bar_time: time in seconds of loop
    bar_width: width as percentage of screen width (0.0-1.0)
    """
    t = pygame.time.get_ticks() / 1000.0 # Get current runtime in seconds
    bar_x = t % bar_time / bar_time # bt: "bar time"

    for node in nodes:
        # u = (node.x - dims[0]) / (dims[2] - dims[0])
        # v = (node.y - dims[1]) / (dims[3] - dims[1])

        distance = abs(node.u - bar_x) # Distance from bar to node
        wrap_distance = abs(node.u - (bar_x - 1.0))

        if (distance < bar_width) or (wrap_distance < bar_width):
            node.color = COLOR_ON
        else:
            node.color = COLOR_OFF

def wipe_left_to_right(nodes: list[Node], bar_time=3, bar_width=0.1):
    """
    nodes: list of nodes to apply effect to
    dims: screen dimensions, tuple: (min_x, min_yy, max_x, max_y)
    bar_time: time in seconds of loop
    bar_width: width as percentage of screen width (0.0-1.0)
    """

    t = pygame.time.get_ticks() / 1000.0 # Get current runtime in seconds
    bar_x = 1.0 - (t % bar_time / bar_time) # bt: "bar time"

    for node in nodes:
        # u = (node.x - dims[0]) / (dims[2] - dims[0])
        # v = (node.y - dims[1]) / (dims[3] - dims[1])

        distance = abs(node.u - bar_x) # Distance from bar to node
        wrap_distance = abs(node.u - (bar_x - 1.0))

        if (distance < bar_width) or (wrap_distance < bar_width):
            node.color = COLOR_ON
        else:
            node.color = COLOR_OFF

def radial_pulse(nodes: list[Node], pulse_time=2.0, pulse_width=0.1):
    t = pygame.time.get_ticks() / 1000.0 # Get current runtime in seconds

    pulse_radius = t % pulse_time / pulse_time

    for node in nodes:
        node_radius = math.sqrt((node.u - 0.5)**2 + (node.v - 0.5)**2)

        distance = abs(node_radius - pulse_radius)

        if (distance < pulse_width):
            # draw_rectangle(node.x, node.y, TRAIN_WIDTH, TRAIN_HEIGHT, COLOR_ON, node.rot)
            node.color = COLOR_ON
        else:
            # draw_rectangle(node.x, node.y, TRAIN_WIDTH, TRAIN_HEIGHT, COLOR_OFF, node.rot)
            node.color = COLOR_OFF
    

def spinner(nodes: list[Node], rev_period=3, num_arms=3, arm_thickness=0.5, center_x=0.5, center_y=0.5, twist=0):
    """
    Renders a spinning fan-like element

    nodes: list of Nodes to edit
    dims: screen dimensions (min_x, min_y, max_x, max_y)
    rev_period: period of 1 revolution in seconds
    num_arms: number of arms on fan
    arm_width: width of each arm from 0-1
    twist: twist the arms. Useful range is about 3 to -3
    """

    t = pygame.time.get_ticks() / 1000.0

    rot_radians = 2 * math.pi * ((t % rev_period) / rev_period) # 0-2pi in `rev_period` seconds
    
    for node in nodes:

        for i in range(num_arms):
            arm_theta = rot_radians + (6.28/num_arms)*i

            # Get relative coordinates
            u = node.u - center_x
            v = node.v - center_y

            r = math.sqrt(u**2 + v**2)

            node_theta = math.atan2(v, u) + math.pi*twist*r
            
            angular_diff = math.atan2(
                math.sin(node_theta - arm_theta),
                math.cos(node_theta - arm_theta),
            )

            if abs(angular_diff) <= arm_thickness:
                node.color = COLOR_ON
                break
            
            node.color = COLOR_OFF
