import math


def time_until_lost_connection(direction_A, direction_B):
    inside_angle = direction_A - direction_B
    inside_angle = inside_angle * math.pi / 180  # convert to radians
    print(math.cos(inside_angle))
    distance_walked = math.sqrt(35 ** 2 / (2 - 2 * math.cos(inside_angle)))
    print(distance_walked)
    hours_walked = distance_walked / 5

    minutes_walked = hours_walked * 60

    return round(minutes_walked, 3)