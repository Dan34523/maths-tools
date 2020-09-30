import random
from tkinter import *

network = []
scale = 100

nodes = int(input("Input how many nodes"))
dimensions = int(nodes ** 0.5)
for row in range(int(dimensions)):
    current_row = []
    for column in range(int(dimensions)):
        if row == column:
            current_row.append(0)
        elif row - 1 <= column <= row + 1 or column - 1 <= row <= column + 1:
            current_row.append(1)
        else:
            current_row.append(0)
    network.append(current_row)
    print(current_row)
root = Tk()

w = Canvas(root, width=(dimensions + 1) * scale, height=(dimensions + 1) * scale)
w.pack()
for i in range(1, dimensions + 1):
    for j in range(1, dimensions + 1):
        w.create_rectangle(i * scale, j * scale, i * scale + dimensions, j * scale + dimensions, fill="red")

for edge_start in range(dimensions):
    for edge_end in range(dimensions):
        if int(network[edge_start][edge_end]) == 1:
            print("start at {}, {}\tend at {}, {}".format(1 + edge_start // dimensions, 1 + edge_start % dimensions, 1 + edge_end // dimensions, 1 + edge_end % dimensions))
            w.create_line(scale * (1 + edge_start // dimensions), scale * (1 + edge_start % dimensions), scale * (1 + edge_end // dimensions), scale * (1 + edge_end % dimensions), fill="black")
root.mainloop()
