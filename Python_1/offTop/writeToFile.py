import csv

file_name = "z.csv"

with open(file_name, "a") as file:
    # rows = csv.reader(file)

    wrtr = csv.writer(file)
    row = ["testName1", 35, "testCity1"]
    wrtr.writerow(row)

# len(file)
# len(rows)
file.close()