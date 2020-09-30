from decimal import Decimal


def work():
    while True:
        threshold_length = int(input("Enter wavelength > "))
        threshold_freq = (3 * 10 ** 8) / (threshold_length * 10 ** -9)
        work_function_j = threshold_freq * (6.63 * 10 ** -34)
        work_function_ev = work_function_j / (1.6 * 10 ** -19)
        print("{:.2E}".format(Decimal(threshold_freq)))
        print("{:.2E}".format(Decimal(work_function_j)))
        print("{:.2E}".format(Decimal(work_function_ev)))


work()
