import os
import pickle # importing pickle module

x = {'a': 1, 'b': 2} # creating dictionary
y = [x, 3, x] # creating list
x['c'] = y # adding new element to dictionary
print('x {} \nBefore pickling: {}'.format(x, y))

fi = open('./8-files/ptest.txt', 'wb') # creating a binary file called ptest
pickle.dump(str(y), fi) # serializing y list
fi.close() # closing file

fi = open('./8-files/ptest.txt', 'rb') # reading the binary file
z = pickle.load(fi) # deserializes the contents of ptest
print('After pickling:', z) # outputs result

# os.remove('./8-files/ptest') # removing the file
