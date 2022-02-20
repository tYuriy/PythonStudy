# [ expr. for val in collection]

a = [0 for i in range(7)]
print (a)

a = [i for i in range(10)]
print (a)

a = [i for i in "string"]
print (a)

a = [i*5 for i in "string"]
print (a)

a = [ord(i) for i in "string"]
print (a)

import random

a = [random.randint(-10,10) for i in range(10)]
print(a)
b = [abs(el) for el in a]
print(b)

