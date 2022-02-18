# Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data,
#   the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered --> It means that the items have a defined order, and that order will not change.
# Unchangeable --> Meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates --> Since tuples are indexed, they can have items with the same value

# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print(len(thistuple))  # length of a tuple

thistuple = ("apple",)  # tuple with one item
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")  # A tuple can contain different data types
print(tuple1)

# Access tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(f'the first item with index 0 is {tuple1[0]}')
print(f'the last item with index -1 is {tuple1[-1]}')
print(thistuple[2:5])  # include first and exclude last
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# ===== Update tuple =====
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# ===== Add Items =====
# 1. Convert into a list: Just like the workaround for changing a tuple,
#   you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)  # convert tuple to a list
y.append("orange")  # add item to a list
thistuple = tuple(y)  # convert list to a tuple

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many),
#   create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")  # exist tuple
y = ("orange",)  # new tuple with one itme to add
thistuple += y  # add tuple to a tuple
print(thistuple)

# ===== Remove Items =====
# 1. Tuples are unchangeable, so you cannot remove items from it,
#   but you can use the same workaround as we used for changing and adding tuple items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# 2. The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# ===== Packing and Unpacking a Tuple =====
# Packing a tuple (in general creating a tuple)
fruits = ("apple", "banana", "cherry")
print(f'Packed (created) tuple {fruits}')
# Unpacking a tuple
(a, b, c) = fruits
print(f'Unpacked tuple is {a} + {b} + {c}')

# Using asterisk 1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  # Assign the rest of the values as a list called "red"
print(green)
print(yellow)
print(red)

# Using asterisk 2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# If the asterisk is added to another variable name than the last,
#   Python will assign values to the variable until the number of values left matches the number of variables left.
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Join Two Tuples
# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 4

print(mytuple)