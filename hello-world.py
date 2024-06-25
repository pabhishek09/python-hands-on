
from math import sqrt

msg = "roll a dice"

print(msg)

msg_cap = msg.capitalize()

print(msg_cap)


names_arr = ["John", "Arya", 1, 2, "Sansa"]

print(names_arr[1])

print(names_arr[0:4])


str1 = "Hello"

str2 = "World"

str = str1 + " " + str2

print(str)

print(str[0 : 5])

for i in range(5):
    if(i%2 ==0):
        print('Even', i)
    else:
        print('Odd', i)


sqrt_16 = sqrt(16)

print('Square root of 16 is', sqrt_16)

input = input('Enter a number: ')

print('You entered', input)