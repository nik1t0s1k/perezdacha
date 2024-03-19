import math


def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


area1 = calculate_triangle_area(3, 4, 5)
area2 = calculate_triangle_area(6, 8, 10)
area3 = calculate_triangle_area(5, 12, 13)

print(area1)
print(area2)
print(area3)
