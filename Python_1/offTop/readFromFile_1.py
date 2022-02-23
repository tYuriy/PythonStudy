file_name = "z.txt"

txt = open(file_name, 'r')
for line in txt:
    print(len(line))
    print(line)
