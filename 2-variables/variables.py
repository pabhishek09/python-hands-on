str1 = "Hello"
str2 = "World"
str_var = str1 + " " + str2
print(str_var)
print(str_var[0 : 5])

is_boolean = True
print(is_boolean)


# data type conversion
float_var = 56.78 # Float variable
int_var = 123 # Integer variable
str_var = "123.2" # String variable

res_int = int(float_var) # Converting float to integer
print(res_int)
print("Type: ", type(res_int)) # Checking type of res_int

res_str = str(float_var) # Converting float to string
print(res_str)
print("Type: ", type(res_str)) # Checking type of res_str

res_ftr = float(str_var) # Converting string to float
print(res_ftr)
print("Type: ", type(res_ftr)) # Checking type of res_ftr


