import random

nodes = []  # Contains the cells themselves. 0 indicates unconnected cell, 1 is connected and 2 is a frontier
frontiers = []  # These are the nodes that have a edge connecting it to the current tree
nodes_connected_to_tree = []
rows = int(input("Enter how many rows > "))
columns = int(input("Enter how many columns > "))
start_row = random.randint(0, rows - 1)
start_column = random.randint(0, columns - 1)


def print_table():
    print("\n\n")
    for row in nodes:
        print(row)


def generate_cells():
    for row in range(rows):
        current_row = []
        for column in range(columns):
            current_row.append(0)
        nodes.append(current_row)
    nodes[start_row][start_column] = 1


def find_neighbours(x, y):
    try:
        if nodes[x + 1][y] == 0:
            nodes[x + 1][y] = 2
            frontiers.append((x + 1, y))
    except IndexError:
        pass

    try:
        if nodes[x - 1][y] == 0:
            nodes[x - 1][y] = 2
            frontiers.append((x - 1, y))
    except IndexError:
        pass

    try:
        if nodes[x][y + 1] == 0:
            nodes[x][y + 1] = 2
            frontiers.append((x, y + 1))
    except IndexError:
        pass

    try:
        if nodes[x][y - 1] == 0:
            nodes[x][y - 1] = 2
            frontiers.append((x, y - 1))
    except IndexError:
        pass


def choose_random_frontier():
    new_node = random.choice(frontiers)
    nodes[new_node[0]][new_node[1]] = 1
    nodes_connected_to_tree.append(new_node)


def empty_cells_exist():
    for row in nodes:
        for column in row:
            if column != 1:
                return True
    return False


generate_cells()
find_neighbours(start_row, start_column)
print_table()
choose_random_frontier()

while empty_cells_exist():
    for node in nodes_connected_to_tree:
        find_neighbours(node[0], node[1])
    print_table()
    choose_random_frontier()