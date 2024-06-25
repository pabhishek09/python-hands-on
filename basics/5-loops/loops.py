# While loop
n = 5
while n > 0: # Will keep on running till n is greater than 0
  print(n)
  n -= 1 # Without this, it will get stuck in infinite loop
  print("End of while loop")

# For loop
for i in range(5, 0, -1):
  print(i)
print("End of for loop")

# range(b) will give the numbers 0, 1, 2, etc., up to, but not including, b.
# range(a, b) will give the numbers a, a+1, a+2, etc., up to, but not including, b.
# range(a, b, c) will give the numbers a, a+c, a+c+c, a+c+c+c, etc., up to (or down to), but not including, b.
