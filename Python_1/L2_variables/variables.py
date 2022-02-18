apples = 10
var_2 = 10000
print(apples)
print(id(apples))
print(id(var_2))

# keywords
import keyword

print(keyword.kwlist)

# quotes
a = 'hello'
print(a)
b = "hello"
print(b)
c1 = '''hello world'''
print(c1)
c2 = '''1st row = hello
2nd row = world'''
print(c2)
c3 = """new 1st row = hello
new 2nd row = world"""
print(c3)

# print("=====================")
str1 = "this is John's ball"
print(str1)
str2 = 'hi, say "hello" to everyone'
print(str2)

print("=====================")
a1 = "Hello "
b1 = "World"
c1 = a1 + b1
print(c1)
print(a1 + b1)
print(c1 * 3)
print(f"c1 length is {len(c1)}")
print(c1.upper())
print(c1.lower())

# numbers
a = 4
b = 1 / 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # division
print(a // b)  # hole number by division
print(a % b)  # the rest from division
print(abs(b - a))  # module, absolute value
print(a ** b)  # extent of a number

a, b, c = 1, 2, 3
print(f'a = {a}, b = {b}, c = {c}')
