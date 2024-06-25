s = ["Mary", 23, "A+"] # List object
print("Original s", s)

name = s[0] # name is now "Mary"
print("Name:", name)

s[1] += 1 # s is now ["Mary", 24, "A+"]
print("Updated s", s)

new_s = [] # Empty list
print("Empty list:", new_s)

zero_list = [0] * 4 # result is [0,0,0,0]
print("Length of zero list:", len(zero_list)) # Should give 4

none_list = [None] * 100 # result is 100 None’s
print("Length of none list:", len(none_list)) # Should give 100

num_list = [2,4] * 3 # result is [2,4,2,4,2,4]
print("Length of number list", len(num_list)) # Should give 6 (num_list has 2 values so 2 * 3) 


my_list = [8,2,10,5,-5] # Initial list
print("Original:", my_list)

length_list = len(my_list) # Finding length of list -> 4
print("Length of list:", length_list)

sorted_list = sorted(my_list) # Sorting the elements of my_list in ascending order
print("After sorting:", sorted_list) # Displaying the results after sorting


my_list = [2,5,8,10] # Initial list
print("Original:", my_list)

my_list.append(25) # Appending a value to my_list
print("After appending:", my_list) # Will now have 25 after 10 in my_list

popped_value = my_list.pop() # Removing 25 and storing it in popped_value variable
print("Popped value:", popped_value)
print("After popping:", my_list) # my_list won't have 25 inside of it

popped_value_two = my_list.pop(2) # Removing value from index 2
print("Popped value two:", popped_value_two)
print("After popping again:", my_list) # my_list now won't have 8 inside of it


i = 2
j = 4

my_list = [2,5,8,10,15,20] # Initial list
print("Original:", my_list)

first_slice = my_list[i:j] # Up to but not including my_list[j]
print(first_slice)

second_slice = my_list[i:] # Starting at my_list[i] and continuing till end (20)
print(second_slice)

third_slice = my_list[:j] # Starting at first index and continuing till my_list[j]
print(third_slice)

fourth_slice = my_list[:] # Copy of my_list
print(fourth_slice)

# Looping over lists

list_1 = [2,5,8,10,15,20] # Initial list

loop1_msg = "Loop 1:"
for e in list_1: # Looping over list_1
    loop1_msg = loop1_msg + " " + str(e)
print(loop1_msg)

loop2_msg = "Loop 2:"
for i in range(0, len(list_1)): # Looping over list_1 using range
    loop2_msg = loop2_msg + " " + str(list_1[i])
print(loop2_msg)
