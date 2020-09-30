def f():
    first_point = input("Enter first point\n> ").replace(" ", "").split(",")
    second_point = input("Enter second point\n> ").replace(" ", "").split(",")

    first_x = float(first_point[0])
    first_y = float(first_point[1])
    second_x = float(second_point[0])
    second_y = float(second_point[1])

    y_midpoint = (first_y + second_y) / 2
    x_midpoint = (first_x + second_x) / 2
    try:
        gradient = (first_x - second_x) / (second_y - first_y)
        y_intercept = -gradient * x_midpoint + y_midpoint
    except ZeroDivisionError:
        gradient = "infinite"
        y_intercept = x_midpoint

    if gradient == "infinite":
        equation = "\nx = {}".format(round(y_intercept, 4))
        print(equation)

    else:
        if gradient == 0:
            equation = "\ny = {}".format(round(y_intercept, 4))

        elif y_intercept > 0:
            equation = "\ny = {}x + {}".format(round(gradient, 4), round(y_intercept, 4))

        elif y_intercept == 0:
            equation = "\ny = {}x".format(round(gradient, 4))

        elif y_intercept < 0:
            equation = "\ny = {}x - {}".format(round(gradient, 4), -round(y_intercept, 4))

        print(equation)
        gradient_tuple = (second_x - first_x, first_y - second_y)
        y_intercept_tuple = (-(first_x - second_x) * (first_x + second_x) + (first_y + second_y) * (second_y - first_y), 2 * (second_y - first_y))
        print("Gradient is {}/{}".format(gradient_tuple[0], gradient_tuple[1]))
        print("Y-intercept is {}/{}\n\n".format(y_intercept_tuple[0], y_intercept_tuple[1]))


f()
