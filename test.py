from math import *


def get_theta_range(equation, count_accuracy=100):
    theta = 0
    theta_increment = count_accuracy / (10 ** 5)
    cartesian_coordinates = []
    count = 0
    tolerance = .01
    while True:
        r = eval(equation)
        x, y = r * cos(theta), r * sin(theta)
        reset_count = True
        for xc, yc in cartesian_coordinates:
            if abs(xc - x) <= tolerance and abs(yc-y) <= tolerance:
                print((x, y), "already exists")
                count += 1
                reset_count = False
                break
        if reset_count:
            print("count reset")
            count = 0

        if count == count_accuracy:
            return theta

        cartesian_coordinates.append((x, y))
        theta += theta_increment


r = get_theta_range("10*sin(4 * theta)")
print(r)
print(2 * pi)

