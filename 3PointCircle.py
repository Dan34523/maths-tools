def perpendicular_bisector(x1, x2, y1, y2):
    y_midpoint = (y1 + y2) / 2
    x_midpoint = (x1 + x2) / 2

    try:
        gradient = (x1 - x2) / (y2 - y1)
        y_intercept = -gradient * x_midpoint + y_midpoint
    except ZeroDivisionError:
        gradient = "infinite"
        y_intercept = x_midpoint

    return gradient, y_intercept


def find_intersection(m1, m2, c1, c2):
    x_intersect = (c2 - c1) / (m1 - m2)
    y_intersect = m1 * x_intersect + c1

    return x_intersect, y_intersect


def find_intersection_infinite_gradient(m1, c1, c2):
    x_intersect = c2
    y_intersect = m1 * c2 + c1

    return x_intersect, y_intersect


def generate_circle_equation(centre_x, centre_y, circumference_x, circumference_y):
    radius_squared = (centre_x - circumference_x) ** 2 + (centre_y - circumference_y) ** 2

    if centre_x > 0:
        if centre_y > 0:
            return "(x - {})^2 + (y - {})^2 = {}".format(centre_x, centre_y, radius_squared)
        elif centre_y < 0:
            return "(x - {})^2 + (y + {})^2 = {}".format(centre_x, abs(centre_y), radius_squared)
        elif centre_y == 0:
            return "(x - {})^2 + y^2 = {}".format(centre_x, radius_squared)

    if centre_x < 0:
        centre_x = abs(centre_x)
        if centre_y > 0:
            return "(x + {})^2 + (y - {})^2 = {}".format(centre_x, centre_y, radius_squared)
        elif centre_y < 0:
            return "(x + {})^2 + (y + {})^2 = {}".format(centre_x, abs(centre_y), radius_squared)
        elif centre_y == 0:
            return "(x + {})^2 + y^2 = {}".format(centre_x, radius_squared)

    if centre_x == 0:
        if centre_y > 0:
            return "x^2 + (y - {})^2 = {}".format(centre_y, radius_squared)
        elif centre_y < 0:
            return "x^2 + (y + {})^2 = {}".format(abs(centre_y), radius_squared)
        elif centre_y == 0:
            return "x^2 + y^2 = {}".format(radius_squared)


def main():
    first_point = input("Enter first point\n> ").replace(" ", "").split(",")
    second_point = input("Enter second point\n> ").replace(" ", "").split(",")
    third_point = input("Enter third point\n> ").replace(" ", "").split(",")

    first_x = float(first_point[0])
    first_y = float(first_point[1])
    second_x = float(second_point[0])
    second_y = float(second_point[1])
    third_x = float(third_point[0])
    third_y = float(third_point[1])

    first_bisector = perpendicular_bisector(first_x, second_x, first_y, second_y)
    second_bisector = perpendicular_bisector(second_x, third_x, second_y, third_y)

    first_gradient = first_bisector[0]
    first_y_intercept = first_bisector[1]
    second_gradient = second_bisector[0]
    second_y_intercept = second_bisector[1]

    if first_gradient != "infinite" and second_gradient != "infinite":
        centre = find_intersection(first_gradient, second_gradient, first_y_intercept, second_y_intercept)
    elif first_gradient == "infinite":
        centre = find_intersection_infinite_gradient(second_gradient, second_y_intercept, first_y_intercept)
    elif second_gradient == "infinite":
        centre = find_intersection_infinite_gradient(first_gradient, first_y_intercept, second_y_intercept)

    circle = generate_circle_equation(centre[0], centre[1], first_x, first_y)
    print(circle)


main()
