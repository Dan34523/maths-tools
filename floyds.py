route_mat = []
distance_mat = []


def input_mat(size, mat):
    print("Enter row:")
    for i in range(size):
        row = input(f"{i + 1} > ").replace(" ", "").split(",")
        row = list(map(lambda x: int(x.replace("inf", "-1")), row))
        mat.append(row)


def print_mat(mat):
    for row in mat:
        print("\t".join(str(x) for x in row))
    print("\n")


def floyd(size, dist_mat, route_mat):
    for i in range(size):
        pivot_row = dist_mat[i]
        pivot_col = [row[i] for row in dist_mat]

        for row_idx in range(size):
            if row_idx == i:
                continue

            for col_idx in range(size):
                if col_idx == i:
                    continue

                if pivot_row[row_idx] == -1 or pivot_col[col_idx] == -1:
                    continue

                new_dist = pivot_row[row_idx] + pivot_col[col_idx]
                current_val = dist_mat[row_idx][col_idx]
                if new_dist < current_val or current_val == -1:
                    dist_mat[row_idx][col_idx] = new_dist
                    route_mat[row_idx][col_idx] = i + 1

        print(f"Iteration {i + 1}:\nDistance Matrix:")
        print_mat(dist_mat)
        print("Route Matrix:")
        print_mat(route_mat)


size = int(input("Size: "))
input_mat(size, distance_mat)
for i in range(size):
    route_mat.append(list(range(1, size + 1)))
floyd(size, distance_mat, route_mat)
