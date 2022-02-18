# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed Dictionaries cannot have two items with the same key
# Duplicate keys will overwrite existing keys:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# Dictionary Items - Data Types The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))