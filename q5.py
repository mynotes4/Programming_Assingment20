"""
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
"""


def missing_num(l):
    l = str_list(l)
    for i in range(1,11):
        if i not in l:
            return i

def str_list(l):
    l = l.split(' ')
    l1 = []
    for i in l:
        l1.append(int(i))
    return l1

l = input("Enter list in following form\n1 2 3 4\n:")
m = missing_num(l)
print("missing_num(",l,") ➞",m)