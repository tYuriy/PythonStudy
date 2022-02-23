import csv

file_name = "z.csv"

with open(file_name, "r") as file:
    rows = csv.reader(file)
    catalog = {}
    for k, v in rows:
        # print(k,v)
        catalog[k] = int(v)
file.close()

for i in range(3):
    k_inp = input()
    v_inp = input()
    if k_inp in catalog:
        catalog[k_inp] = catalog[k_inp] + int(v_inp)
    else:
        catalog[k_inp] = int(v_inp)

with open(file_name, "w") as file:
    rows = csv.writer(file)
    for k, v in catalog.items():
        rows.writerow([k,v])

#     num_lines = sum(1 for line in file)
#     print(num_lines)
#
#
# file.close()
