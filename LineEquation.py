while True:
    gradient = float(input("Gradient > "))
    point = [float(i) for i in input("Point > ").replace(" ", "").split(",")]
    y_intercept = -1 * gradient * point[0] + point[1]
    print("y = {}x + {}".format(gradient, y_intercept))
