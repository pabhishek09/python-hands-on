# A tuple consists of two or more values separated by commas and enclosed in parentheses, for example, ("John", 23)

tup1 = (1, 2, 3) # Tuple of integers
print(tup1)

tup2 = (7, "Great", 1.52, True) # Tuple of mixed data types
print(tup2)


x = (1, 2, 3) # x now holds the tuple (1, 2, 3)
print("Tuple:", x)

y = x[1] # y is now 2 (tuples are zero-indexed)
print("Value of x[1]:", y)

z = x[-1] # z is now 3 (tuples support negative indexing)
print("Value of x[-1]:", z)
