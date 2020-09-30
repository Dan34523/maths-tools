def generate_equation(x1, y1, x2, y2, given_radius):
    global equation
    try:
        gradient = (x1 - x2) / (y2 - y1)
    except ZeroDivisionError:
        gradient = "infinite"

    if gradient != "infinite":
        y_intercept = -gradient * x1 + y1
    else:
        y_intercept = x1

    calculated_radius_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2

    if calculated_radius_squared != given_radius ** 2:
        print("Invalid data given!\nEnter data again.\n")
        main()

    if gradient == "infinite":
        equation = "\nx = {}".format(y_intercept)  # Here y-intersept is actually the x-intercept but I'm lazy

    elif y_intercept > 0:
        equation = "\ny = {}x + {}".format(round(gradient, 4), round(y_intercept, 4))

    elif y_intercept == 0:
        equation = "\ny = {}x".format(round(gradient, 4))

    elif y_intercept < 0:
        equation = "\ny = {}x - {}".format(round(gradient, 4), -round(y_intercept, 4))

    print(equation)


def main():
    centre = input("Enter circle centre\n> ").replace(" ", "").split(",")
    centre_x = float(centre[0])
    centre_y = float(centre[1])
    radius = float(input("Enter radius of circle\n> "))

    tangent_point = input("Enter the point of\ntangent\n> ").replace(" ", "").split(",")
    tangent_x = float(tangent_point[0])
    tangent_y = float(tangent_point[1])

    generate_equation(tangent_x, tangent_y, centre_x, centre_y, radius)


main()
