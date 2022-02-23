file_name = "z.txt"

txt = open(file_name, 'r')
cnt=0
for line in txt.readline():
    print(line)
    cnt+=1
print(cnt)
