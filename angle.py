import math

from util import remove_negative

def radians_to_angle(radians):
    '''
    radians ex:
    3P/4
    7P/4
    '''
    numbers = radians.split("/")
    numerator = 0
    if(len(numbers) > 1):
        denominator = int(numbers[1])
    else:
        denominator = 1
    for i in range(len(numbers[0])):
        if(numbers[0][i] >= '0' and numbers[0][i] <= '9'):
            numerator *= 10
            numerator += int(numbers[0][i])
        elif(numbers[0][i] == 'P'):
            break

    return numerator*180/denominator
    

def angle_to_radians(angle):
    '''
    Only integer angle
    '''
    numerator = angle
    denominator = 180
    for i in reversed(range(1, 180)):
        if(numerator%i == 0 and denominator%i == 0):
            numerator = int(numerator/i)
            denominator = int(denominator/i)
            return str(numerator) + "P/" + str(denominator)


def tan_to_angle(tan, quadrant):
    if(tan == 0):
        return 0
    tan, _ = remove_negative(tan)
    angle = None
    smallest_difference = None

    # we can use 8999 and i/100 for better precision
    for i in range(9000):
        local_angle = i/100
        local_tan = math.tan(math.radians(local_angle))
        
        difference, _ = remove_negative(tan - local_tan)

        if(smallest_difference is None or difference < smallest_difference):
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
