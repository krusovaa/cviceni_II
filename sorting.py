import random


def random_list(n):
    return [chr(random.randrange(65, 65 + 26)) for _ in range(n)]


def select_sort(alist):
    x = alist
    for i in range(0, len(x) - 1):  # kdyz setrideno n-1 prvku, posledni je automaticky take setrideny
        imin = i  # Inicializace indexu minima
        for j in range(i, len(x)):  # Hledani minima
            if x[j] < x[imin]:  # porovnavani promennych pomoci indexu
                imin = j  # Jeho index
        temp = x[i]  # Prohozeni promennych
        x[i] = x[imin]
        x[imin] = temp
    # sort list using select sort
    # until list is sorted
    # select minimum form unsorted part
    # swap minimum with first unsorted element
    return alist


def quick_sort(alist):
    qs(alist, 0, len(alist))


def qs(alist, l, r):
    # check is list is long enough
    if len(alist) < 3:
        print('List is not long enough.')
        exit()
    # choose pivot
    pivot = alist[0]
    # call presort list
    presort_list(alist, 0, len(alist), pivot)
    # prepare indices to the left and right part
    outr1 = i
    outl2 = j
    # recursively sort left and right part
    if l < j:
        qs(alist, l, outr1)
    if r > i:
        qs(alist, outl2, r)
    return alist


def presort_list(alist, l, r, pivot):
    p = pivot
    # move right index to the left
    i = 0
    j = r - 1
    # while True:
    while True:
        # While left index < right boundary and left element < pivot:
        while i < r and alist[i] <= p:
            # move left index to the right
            i = i + 1
        # while right index > left boundary and right element  >= pivot:
        while j > l and alist[j] >= p:
            # move right index to the left
            j = j - 1
        # if left index  >= right index
        if i >= j:
            break
        # swap elements on left and right index
        temp = alist[i]
        alist[i] = alist[j]
        alist[j] = temp
    # return right index, left index # in the end, right index <= left index
    return i, j


alist = random_list(20)
print(alist)
quick_sort(alist)
# presort_list(alist, 0, len(alist), alist[0])
print(alist)
