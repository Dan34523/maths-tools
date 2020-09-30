from math import ceil


class Bin:
    def __init__(self, max_size):
        self.size = max_size
        self.space_used = 0
        self.contents = []

    def add_item(self, item):
        self.space_used += item
        self.contents.append(item)


first_fit_decreasing = int(input("Enter 1 if you need\nfirst fit decreasing\n> "))
items = [float(i) for i in input("Enter list of items:\n").replace(" ", "").split(",")]
if first_fit_decreasing == 1:
    items.sort(reverse=True)
total_size = sum(items)

bin_size = int(input("How much can each\nbin store? > "))
lower_bound = ceil(total_size / bin_size)

bins = []
for i in range(lower_bound + 1):
    new_bin = Bin(bin_size)
    bins.append(new_bin)

for item in items:
    i = 0
    for bin in bins:
        i += 1
        if bin.size - bin.space_used >= item:
            bin.add_item(item)
            break
    if i >= len(bins):
        new_bin = Bin(bin_size)
        bins.append(new_bin)
        new_bin.add_item(item)

print("Lower bound of bins:\n{}".format(lower_bound))
for i in range(len(bins) - 1):
    print("Bin {}: {}".format(i + 1, bins[i].contents))
