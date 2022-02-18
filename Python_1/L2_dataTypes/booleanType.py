# boolean
print(f'Any positive number is {bool(1)}')
print(f'Any negative number is {bool(-1)}')
print(f'Zero is always {bool(0)}')
print(f'Empty value or None is {bool(None)}')
print(f'Not empty strnig is {bool("a string")}')
print(f'Empty string is {bool("")}')
emptyArr = []
print(f'Empty array is {bool(emptyArr)}')
notEmptyArr = [5]
print(f'Not empty array is {bool(notEmptyArr)}')
