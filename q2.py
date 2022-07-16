"""
Question2
Given a list of numbers, create a function which returns the list but with each element's index
in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number
at index 1, etc...
Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
"""

def add_indexes(l):
    l = str_list(l)
    l1 = []
    for i in range(len(l)):
        l1.append(i + l[i])
    return l1

def str_list(l):
    l = l.split(' ')
    l1 = []
    for i in l:
        l1.append(int(i))
    return l1

l = input("Enter list in following form\n1 2 3 4\n:")
l1 = add_indexes(l)
print("add_indexes(",l,") ➞",l1)