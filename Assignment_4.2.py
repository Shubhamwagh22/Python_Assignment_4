# Write a Python program to triple all numbers of a given list of integers. Use Python map.

lst = [1, 2, 3, 4, 5, 6, 7]

def num(lst):
    return (lst * 3)
triple = list(map(num,lst))
print ("Triple of list numbers :",triple)
