import math

from util import remove_negative

def radians_to_angle(radians):
    pass

def angle_to_radians(angle):
    pass

def tan_to_angle(tan, quadrant):
    if(tan == 0):
        return 0
    tan, _ = remove_negative(tan)
    angle = None
    smallest_difference = 1000000

    # we can use 8999 and i/100 for better precision
    for i in range(899):
        local_angle = i/10
        local_tan = math.tan(math.radians(local_angle))
        
        difference, _ = remove_negative(tan - local_tan)

        if(difference < smallest_difference):
            smallest_difference = difference
            angle = local_angle

    if(quadrant == 1):
        return angle
    elif(quadrant == 2):
        return 180 - angle
    elif(quadrant == 3):
        return 180 + angle
    elif(quadrant == 4):
        return 360 - angle
