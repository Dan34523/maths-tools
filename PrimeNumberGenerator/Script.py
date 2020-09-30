m = 77232917

while True:
    x = (2 ** m) - 1
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 11 != 0 and x % 13 != 0:
        with open("Result.txt", "a") as f:
            f.write("\nM{}".format(m))
    m += 1
