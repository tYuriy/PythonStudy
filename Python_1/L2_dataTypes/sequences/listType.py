# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data,
#   the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered --> Means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Note: There are some list methods that will change the order, but in general: the order of the items will not change.
# Changeable --> Meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates --> Since lists are indexed, lists can have items with the same value

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# list = array
div = "=========================================="

aList1 = [5, 's', 3, "string", 2, True, [1, 2, 'left']]
print(aList1)

for el in aList1:
    print(el)

aList2 = [5, 6, 3, 8, 2, 6]
print(f'------- source list is {aList2}')
# add elements (at the end only
aList2.append(4)  # add element at the end
print(f'list after add element {aList2}')
# remove element by position
aList2.pop(1)
print(f'list after remove element with index 1 {aList2}')
# remove first item with specified value
aList2.remove(8)
print(f'list after remove element with value 8 {aList2}')

print(f'source list is {aList2}')
# reverse function
aList2.reverse()
print(f'reversed list is {aList2}')
# reverse function
aList2.sort()
print(f'sorted list is {aList2}')

print(div)
print(f'source list is {aList2}')
# get item by index
print(f'the first item with index 0 is {aList2[0]}')
print(f'the last item with index -1 is {aList2[-1]}')
print(f'part of the list from index 1 to 4 (not includes) is {aList2[1:4]}')

print(f'index of the first element (with specified value, 6 in the example) in the list is {aList2.index(6)}')
# set new value by index
aList2[0] = 666
print(f'change value by index of the element {aList2}')
print(div)

aList3 = aList2.copy()
print(f'list is a copy of an array {aList3}')
aList3.clear()
print(f'list after use the clear function {aList3}')
val = 6
cnt = aList2.count(val)

# print(cnt)
print(f'number of elements with specified value (6 in the example) {cnt}')
print(f'number of elements {len(aList2)}')

list4 = [1, 2, 3]

list5 = ['a', 'b', 'c']

list6 = list4 + list5  # can concatenate list to list
print(list6)
print(str(list4) + str(list5))
list4.extend('str')
print(list4)

# Loop lists
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print(thisList[i])

thisList = ["apple", "banana", "cherry"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1
