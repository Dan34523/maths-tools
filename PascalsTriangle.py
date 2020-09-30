def pascal(row):
    line = [1]
    for k in range(row):
        line.append(int(line[k] * (row - k) / (k + 1)))
    return line


print(pascal(int(input("Enter the row for Pas\n-cal's Tiangle\n> "))))
