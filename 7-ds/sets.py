# A set is a collection of values that are not necessarily all the same type. To write a set, use braces around a comma-separated list. Take a look at a few examples using sets below:

int_set = {1, 2, 3, 4, 5} # set having all integer values
print(int_set)

s = {10, "ten", "X", "X"} # A set having mixed data type values
print(s) # this will give (10, "ten", "X") since sets have no duplicate elements

for elem in s:
  print('Traversing s', elem)

print("In:", 10 in s) # checking if 10 is present in s -> True
print("Not in:", "TEN" not in s) # checking if TEN is not present in s -> True


# traversing through set and printing its values
for elem in s: 
  print('Traversing s', elem)


set_to_list = list(s) # converting from set to list
print(set_to_list)
print(type(set_to_list))

my_list = [1, 'world', 25] # list
print(my_list)
print(type(my_list))

list_to_set = set(my_list) # converting from list to set
print(list_to_set)
print(type(list_to_set))

