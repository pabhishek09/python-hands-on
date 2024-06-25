file_path = './8-files/hello.txt' # file path

file = open(file_path) # opening and reading file
data = file.read() # reading entire file as single string
print(data) # printing the contents of file
file.close() # closing the file


# using with operator to write to file
with open(file_path, 'w') as file: # added the w mode in open
  file.write('Hey! New message got written right now') # using write method to write to file

# using with operator to read the text file contents after writing
with open(file_path, 'r') as file:
  data = file.read()
  print(data)

