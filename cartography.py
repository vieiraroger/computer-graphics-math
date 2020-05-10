import math
import numpy as np

from angle import tan_to_angle

def quadrant(x, y):
    if(x >= 0 and y >= 0):
        return 1
    elif(x <= 0 and y >= 0):
        return 2
    elif(x <= 0 and y <= 0):
        return 3
    else:
        return 4


def polar_to_cartesian(distance, angle):
    '''
    Input:
    - distance
    - angle
    Output:
    - X cartesian point
    - Y cartesian point
    '''
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    return distance*cos, distance*sin


def carteian_to_polar(x, y):
    '''
    Input:
    - X cartesian point
    - Y cartesian point
    Output:
    - distance
    - angle
    '''
    # sohcahtoa
    distance = math.sqrt(x*x + y*y)


    angle = tan_to_angle(y/x, quadrant(x, y))
    return distance, angle


def distance_bettewen_two_points(x1, y1, x2, y2):
    x_dif = x1 - x2
    y_dif = y1 - y2
    return math.sqrt(x_dif * x_dif + y_dif * y_dif)


def print_mid_point(x1, y1, x2, y2, x3, y3):
    pass