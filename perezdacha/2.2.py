import math


def calculate_cone_volume(radius, height):
    base_area = math.pi * radius ** 2
    volume = (1 / 3) * base_area * height
    return volume


volume1 = calculate_cone_volume(5, 10)
print(volume1)

radius2 = 3.5
height2 = 7
volume2 = calculate_cone_volume(3.5, 7)
print(volume2)
