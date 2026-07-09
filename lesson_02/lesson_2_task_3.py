import math


def square(side):
    area = side * side

    if type(side) != int:
        area = math.ceil(area)

    return area


result = square(5.5)
print(result)