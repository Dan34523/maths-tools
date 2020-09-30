import math


def degrees(angle):
    return 180 * (angle / math.pi)


class Vector:
    def __init__(self, i, j, k=None):
        if k is not None:
            self.vector = [i, j, k]
        else:
            self.vector = [i, j]
        self.dimensions = len(self.vector)
        self.magnitude = 0
        self.i_component = self.vector[0]
        self.j_component = self.vector[1]

        self.ijk_squares_sum = self.i_component ** 2 + self.j_component ** 2

        if self.dimensions == 3:
            self.k_component = self.vector[2]
            self.ijk_squares_sum += self.k_component ** 2

        self.magnitude_squared = self.ijk_squares_sum


def check_not_identical_size(vector_a, vector_b):
    if vector_a.dimensions == vector_b.dimensions:
        return False
    else:
        return True


def dot_product(vector_a, vector_b):
    if vector_a.dimensions != vector_b.dimensions:
        print("Invalid")
        return None

    running_total = 0
    for component in range(vector_a.dimensions):
        running_total += vector_a.vector[component] * vector_b.vector[component]

    return running_total


def cross_product(vector_a, vector_b):
    cross_i_component = vector_a.j_component * vector_b.k_component - vector_a.k_component * vector_b.j_component
    cross_j_component = -1 * (vector_a.i_component * vector_b.k_component - vector_a.k_component * vector_b.i_component)
    cross_k_component = vector_a.i_component * vector_b.j_component - vector_a.j_component * vector_b.i_component

    cross_vector = Vector(cross_i_component, cross_j_component, cross_k_component)

    return cross_vector


def angle_between_lines(vector_a, vector_b, force_acute=True):
    if check_not_identical_size(vector_a, vector_b):
        return
    a_dot_b = dot_product(vector_a, vector_b)
    mod_a_squared = vector_a.magnitude_squared
    mod_b_squared = vector_b.magnitude_squared

    cos_theta = a_dot_b / math.sqrt(mod_a_squared * mod_b_squared)

    if force_acute:
        angle = math.acos(abs(cos_theta))
    else:
        angle = math.acos(cos_theta)

    return round(degrees(angle), 6)


def angle_between_plane_and_line(plane_normal, line):
    return round(90 - angle_between_lines(plane_normal, line, force_acute=True), 6)


def angle_between_planes(plane1_normal, plane2_normal):
    return round(180 - angle_between_lines(plane1_normal, plane2_normal, force_acute=False), 6)


option = input("1. Dot Product\n2. Cross Product\n3. Angles\n")
while option not in ["1", "2", "3"]:
    print("Invalid input\n")
    option = input("1. Dot Product\n2. Cross Product\n3. Angles\n")

option = int(option)

if option == 1:
    first_vector = [float(i) for i in input("Enter first vector\n> ").replace(" ", "").split(",")]
    second_vector = [float(i) for i in input("Enter second vector\n> ").replace(" ", "").split(",")]
    vector1 = Vector(first_vector[0], first_vector[1], first_vector[2])
    vector2 = Vector(second_vector[0], second_vector[1], second_vector[2])
    print(dot_product(vector1, vector2))

if option == 2:
    first_vector = [float(i) for i in input("Enter first vector\n> ").replace(" ", "").split(",")]
    second_vector = [float(i) for i in input("Enter second vector\n> ").replace(" ", "").split(",")]
    vector1 = Vector(first_vector[0], first_vector[1], first_vector[2])
    vector2 = Vector(second_vector[0], second_vector[1], second_vector[2])
    cross_product = cross_product(vector1, vector2)

    print("{}, {}, {}".format(cross_product.i_component, cross_product.j_component, cross_product.k_component))

if option == 3:
    angle_option = input("1. 2 Lines\n2. 2 Lines Acute\n3. Line & Plane\n4. 2 Planes\n")
    while angle_option not in ["1", "2", "3", "4", "5"]:
        print("Invalid input\n")
        angle_option = input("1. 2 Lines\n2. Line and Plane\n3. 2 Planes\n")

    angle_option = int(angle_option)
    if angle_option == 1:
        first_vector = [float(i) for i in input("Enter first vector\n> ").replace(" ", "").split(",")]
        second_vector = [float(i) for i in input("Enter second vector\n> ").replace(" ", "").split(",")]
        vector1 = Vector(first_vector[0], first_vector[1], first_vector[2])
        vector2 = Vector(second_vector[0], second_vector[1], second_vector[2])

        angle = angle_between_lines(vector1, vector2, force_acute=False)

    if angle_option == 2:
        first_vector = [float(i) for i in input("Enter first vector\n> ").replace(" ", "").split(",")]
        second_vector = [float(i) for i in input("Enter second vector\n> ").replace(" ", "").split(",")]
        vector1 = Vector(first_vector[0], first_vector[1], first_vector[2])
        vector2 = Vector(second_vector[0], second_vector[1], second_vector[2])

        angle = angle_between_lines(vector1, vector2, force_acute=True)

    if angle_option == 3:
        first_vector = [float(i) for i in input("Enter first vector\n> ").replace(" ", "").split(",")]
        second_vector = [float(i) for i in input("Enter plane normal\n> ").replace(" ", "").split(",")]
        vector1 = Vector(first_vector[0], first_vector[1], first_vector[2])
        vector2 = Vector(second_vector[0], second_vector[1], second_vector[2])

        angle = angle_between_plane_and_line(vector2, vector1)

    if angle_option == 4:
        first_vector = [float(i) for i in input("Enter first normal\n> ").replace(" ", "").split(",")]
        second_vector = [float(i) for i in input("Enter second normal\n> ").replace(" ", "").split(",")]
        vector1 = Vector(first_vector[0], first_vector[1], first_vector[2])
        vector2 = Vector(second_vector[0], second_vector[1], second_vector[2])

        angle = angle_between_planes(vector1, vector2)

    print(angle)
