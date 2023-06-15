# Write a Python program to square the elements of a list using map() function.

lst = [4, 5, 2, 9]
def num (lst):
    return (lst ** 2)

square = list(map(num,lst))
print("Square the elements of the list :",square)