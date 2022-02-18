num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
itr = iter(num_list)
mid = int(len(num_list) / 2)

for i in range(mid):
    print(f'first set of values {next(itr)}')

for j in range(mid, len(num_list)):
    print(f'second set of values {next(itr)}')

# class OddNum:
#     def __init__(self):
#         self.x = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         cur, self.x = self.x, self.x +1
#         return cur
#
# for item in OddNum():
#     if item%1000000 == 0:
#         print(item)

class MySequence:
    def __init__(self, stop_iter):
        self.stop = stop_iter
    def __getitem__(self, key):
        if key>self.stop:
            raise IndexError ("That's enough!")
        return key*10

x = MySequence(10)
y = iter(x)
for item in y:
    print(item)

