from random import randint
from tkinter import *

root = Tk()
root.title("Random Sequence Generator")
root.resizable(0, 0)

nth_term = ""


def linearfunc():
    global nth_term
    linear.grid_forget()
    quadratic.grid_forget()
    geometric.grid_forget()

    a = randint(1, 10)
    b = randint(1, 10)
    sequencetext = ""

    for n in range(1, 6):
        sequencetext = "{}{}, ".format(sequencetext, (a * n) + b)

    sequencetext = sequencetext[:len(sequencetext) - 2]
    sequence.config(text=sequencetext)
    sequence.grid(padx=50, pady=(25, 0))
    showanswer.grid(padx=50, pady=(5, 25))

    nth_term = "{}n + {}".format(a, b)


def quadraticfunc():
    global nth_term
    linear.grid_forget()
    quadratic.grid_forget()
    geometric.grid_forget()

    a = float(randint(1, 4) / 2)
    b = float(randint(1, 3))
    c = float(randint(1, 5))
    sequencetext = ""

    for n in range(1, 6):
        sequencetext = "{}{}, ".format(sequencetext, (a * n * n) + (b * n) + c)

    sequencetext = sequencetext[:len(sequencetext) - 2]
    sequence.config(text=sequencetext)
    sequence.grid(padx=50, pady=(25, 0))
    showanswer.grid(padx=50, pady=(5, 25))

    nth_term = "{}n^2 + {}n + {}".format(a, b, c)


def geometricfunc():
    global nth_term
    linear.grid_forget()
    quadratic.grid_forget()
    geometric.grid_forget()

    a = randint(1, 5)
    b = randint(2, 5)
    sequencetext = ""

    for n in range(1, 6):
        sequencetext = "{}{}, ".format(sequencetext, (a * (b ** (n - 1))))

    sequencetext = sequencetext[:len(sequencetext) - 2]
    sequence.config(text=sequencetext)
    sequence.grid(padx=50, pady=(25, 0))
    showanswer.grid(padx=50, pady=(5, 25))

    nth_term = "{} x {}^n-1".format(a, b)


def showanswerfunc():
    showanswer.grid_forget()
    answer.config(text=nth_term)
    answer.grid(row=1, padx=50, pady=20)


linear = Button(root, text="Linear", width=20, command=linearfunc)
quadratic = Button(root, text="Quadratic", width=20, command=quadraticfunc)
geometric = Button(root, text="Geometric", width=20, command=geometricfunc)

sequence = Label(root, text="", font="SegoeUI 16 bold")
showanswer = Button(root, text="Show Answer", command=showanswerfunc)
answer = Label(root, text="", font="SegoeUI 16 bold")

linear.grid(pady=(20, 2), padx=50)
quadratic.grid(row=1, padx=50)
geometric.grid(row=2, pady=(2, 20), padx=50)

if __name__ == "__main__":
    root.mainloop()
