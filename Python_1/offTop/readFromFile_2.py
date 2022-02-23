file_name = "z.txt"

txt = open(file_name, 'r')
for line in txt.read():
    print(line)
