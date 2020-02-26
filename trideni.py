import random

def random_list(n):
    return [random.randrange(0, 1000) for _ in range(n)]

def select_sort(alist):
    for i in alist:

    # sort list using select sort
    # until list is sorted
        # select minimum form unsorted part
        # swap minimum with first unsorted element
    return alist


alist = random_list(20)
print(alist)
print(select_sort(alist))