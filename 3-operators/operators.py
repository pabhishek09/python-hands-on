print(10 + 20) # Adding integers
f1 = 23.25
f2 = 1.72
print(f1 + f2) # Adding float numbers togehter

x_prin = 12
y_prin = 5.5
print(x_prin + y_prin) # Adding integer with float

print(20 - 10) # Subtracting integers
f1 = 23.25
f2 = 1.72
print(f1 - f2) # Subtracting decimal numbers togehter

x_prin = 12
y_prin = 5.5
print(x_prin - y_prin) # Subtracting integer with float

print(20 * 10) # Multiplying integers

f1 = 23.25
f2 = 1.72
print(f1 * f2) # Multiplying decimal numbers togehter

x_prin = 12
y_prin = 5.5
print(x_prin * y_prin) # Multiplying integer with float

print(20 ** 10) # Using integer as both the base and exponent 

f1 = 23.25
f2 = 1.72
print(f1 ** f2) # Using float as both the base and exponent 

x_prin = 12
y_prin = 5.5
print(y_prin ** x_prin) # Using float as the base and integer as the exponent 
print(x_prin ** y_prin) # Using integer as the base and float as the exponent 

print(20 / 10)  # dividing integers

f1 = 23.25
f2 = 1.72
print(f1 / f2) # dividing floats

x_prin = 12
y_prin = 5.5
print(y_prin / x_prin) # dividing numerator float with integer denominator

print('Division', 10 / 4)  # Performing division on the two integer operands
print('Integer division', 10 // 4) # Performing integer division on the two integer operands

print('Division with floats', 10.0 / 4.0) # Performing division on the two float operands
print('Integer division with floasts', 10.0 // 4.0) # Performing integer division on the two float operands

print(20 % 7) 
print(10 % 3) 
print(6 % 2)
print(24.4 % 2.5)  # A float reminder

print(2 == 2 or 4 > 5) # Checking "or" short-circuit nature -> True
print(2 == 5 and 10 > 5) # Checking "and" short-circuit nature (left expression False) -> False
print(5 == 5 and 10 > 5) # Left expression True so checks right expression -> True

check_not = 5 > 2
print(check_not) # Original result -> True
print(not check_not) # Result after applying Not Operator -> False

x = 13 # Assigning the value 13 to a variable x
y = 5 # Assigning the value 5 to a variable y

x += y # Shortcut for x = x + y 
print(x)

x -= y # Shortcut for x = x - y
print(x)

x *= y # Shortcut for x = x * y
print(x)

x /= y # Shortcut for x = x / y
print(x)

n = 10
x = (n := 3 * n) + 1 # Using walrus operator
print(n) # Should give 30
print(x) # Should give 31
