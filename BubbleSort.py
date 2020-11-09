def bubble_sort_ascending(alist, asc):
    comparisons = 0
    swaps = 0
    for passnum in range(len(alist) - 1, 0, -1):
        temp_list = [int(i) for i in alist]
        for i in range(passnum):
            comparisons += 1
            if asc == 1:
                if alist[i] > alist[i + 1]:
                    temp = alist[i]
                    alist[i] = alist[i + 1]
                    alist[i + 1] = temp
                    swaps += 1
            else:
                if alist[i] < alist[i + 1]:
                    temp = alist[i]
                    alist[i] = alist[i + 1]
                    alist[i + 1] = temp
                    swaps += 1
        if temp_list == alist:
            print(comparisons)
            print(swaps)
            return
        print(alist)



ascending = int(input("Enter 1 if you\nwant ascending > "))
list_entred = input("Enter a list of items\n> ").replace(" ", "").split(",")
alist = [int(i) for i in list_entred]
bubble_sort_ascending(alist, ascending)
print("The final list is:\n{}".format(alist))
