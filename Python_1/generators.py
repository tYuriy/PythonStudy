# Generator function
# A function or method which uses the yield statement is called a generator function
# Generator function, when called, always returns an iterator object which can be used to execute the body of the
# function: calling the iterator’s iterator.__next__() method will cause the function to execute until it provides a
# value using the yield statement
# When the function executes a return statement or falls off the end, a StopIteration exception is raised and the
# iterator will have reached the end of the set of values to be returned


def count_generator():
    n = 0
    print('First')
    while True:
        print('Second')
        yield n
        n += 1
        print('Third')
        yield n
        n += 10


counter = count_generator()
print(next(counter))
print("===========")
print(next(counter))
print("===========")
print(next(counter))
print("===========")
print(next(counter))
print("===========")
print(next(counter))
print("===========")


def fibonacci(stop):
    a, b = 0, 1
    while b <= stop:
        yield b
        a, b = b, a + b


# first example
x =  fibonacci(21)
for item in x:
    print(item)

# second example
x = fibonacci(21)
while True:
    try:
        print(next(x))
    except StopIteration:
        break

# generator.send(value)
# • Resumes the execution and “sends” a value into the generator function
# • The value argument becomes the result of the current yield expression
# • The send() method returns the next value yielded by the generator, or raises StopIteration if the generator exits
# without yielding another value
# • When send() is called to start the generator, it must be called with None as the argument, because there is no yield
# expression that could receive the value

def count (start =0, step = 1, stop = 10):
    # count() --> 0 1 2 3 4 ...
    # count(2.5,0.5,4) --> 2.5 3.0 3.5 4.0
    n = start
    while n< stop:
        val = yield n
        if val is not None:
            n = val
        n+=step

it = count(stop = 20)
for item in it:
    print(item)
    if item>3:
        it.send(18)

# Generator expression
# • A generator expression yields a new generator object
# • Generator expression syntax is the same as for comprehensions, except that it is enclosed in parentheses instead of
# brackets or curly braces
# • To avoid interfering with the expected operation of the generator expression itself, yield and yield from expressions
# are prohibited in the implicitly defined generator (in Python 3.7, such expressions emit DeprecationWarning when
# compiled, in Python 3.8+ they will emit SyntaxError)

my_generator = (i for i in range(10))
# my_generator
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

