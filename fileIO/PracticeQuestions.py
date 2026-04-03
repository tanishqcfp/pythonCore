# Problem 1: File Line Counter
# with open("demo.txt","r") as f:
#     lines = f.readlines()
#     print(len(lines))


# Problem 2: File Overwriter
# with open("demo1.txt","w") as f:
#     f.write("NEW EDITED FILE\n")


# Problem 3: File Uppercase Converter
# with open("demo.txt","r") as f:
#     data = f.read()

#     new_data = data.upper()

# with open("output.txt","w") as f:
#     f.write(new_data)

# Problem 4: CSV Column Extractor

import csv

# with open("data.csv","r") as f:
#     reader = csv.reader(f)

#     next(reader) # skip header

#     with open("newoutput.txt","w") as f:
#         for row in reader:
#             f.write(row[0] + "\n")


# Problem 6: Error Frequency Counter

# count = 0
# with open("logFile.txt","r") as f:
#     for line in f:
#         if "ERROR" in line:
#             count += 1

# print(count)


#calculte sales in a CSV file
# total = 0

# with open("sales.csv", "r") as f:
#     reader = csv.reader(f)
    
#     next(reader)  # skip header
    
#     for row in reader:
#         total += int(row[2])  # Amount column

# print("Total Sales:", total)