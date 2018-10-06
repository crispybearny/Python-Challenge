import os
import csv

csvpath = os.path.join("budget_data.csv")

print (csvpath)

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print ([row for row in reader])
 