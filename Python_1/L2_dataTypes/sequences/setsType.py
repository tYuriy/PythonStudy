# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered --> means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#
# Unchangeable --> meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed --> Sets cannot have two items with the same value.
div = "=========================================="

aset = {1, 2, 3, 4, 5, 1, 23, 3, 6, 9, 7, 6, 5, 1, 0}
print(aset)
# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
print(type(thisset))

# Access Items
# You cannot access items in a set by referring to an index or a key.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# ===== Change Items =====
# Once a set is created, you cannot change its items, but you can add new items.

# ===== Add Items =====
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets. To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
# The object in the update() method does not have to be a set,
#   it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"setEl1", "setEl2", "setEl3"}
mylist = ["listEl1", "listEl2"]
myTuple = ("tupleEl1", "tupleEl2")
myString = "word"

thisset.update(mylist)
thisset.update(myTuple)
thisset.update(myString)

print(thisset)

# ===== Remove Item =====
# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove the last item.
#   Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.

# Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
try:
    print(thisset)
except NameError:
    print('Set with name "thisset" does not exist')

# Loop Items
# You can loop through the set items by using a for loop:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# print("apple" in thisset)

print(div)
# ===== Join Two Sets =====
# The union() method returns a new set containing all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print(div)
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.
print(div)
# Keep ONLY the Duplicates --> The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
print(div)
# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
print(div)
# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
print(div)
# The symmetric_difference() method will return a new set,
#   that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)