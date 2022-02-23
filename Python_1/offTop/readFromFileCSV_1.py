import csv

file_name = "z.csv"

txt = open(file_name, 'r+')

# for line in txt.readlines():
#     print(line)

catalog = [line for line in txt.readlines()]
print(catalog)


