import random

round = 1

urn = []
black_beans = int(input("Black beans > "))
white_beans = int(input("White beans > "))


def initialise_urn():
    for i in range(white_beans):
        urn.append("white")
    for i in range(black_beans):
        urn.append("black")


def compare_bean():
    global round
    bean1 = random.choice(urn)
    urn.remove(bean1)

    bean2 = random.choice(urn)
    urn.remove(bean2)

    if bean1 == bean2:
        urn.append("black")
    else:
        urn.append("white")

    number_of_white = urn.count("white")
    number_of_black = urn.count("black")

    print("Round {}: {} and {}. {} white and {} black in urn".format(round, bean1, bean2, number_of_white, number_of_black))
    round += 1


initialise_urn()

while len(urn) > 1:
    compare_bean()

print(urn)
