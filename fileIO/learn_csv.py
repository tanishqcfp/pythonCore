import csv

# #Read and print in a CSV file
# with open("coding_skills.csv","r") as f:
#     reader = csv.reader(f)
    
#     # for row in reader:
#     #     print(row)

# #___________________________________________________________________________________________________________________________#

# data = [
#     ["name", "age", "city"],
#     ["Tanishq", 22, "Delhi"],
#     ["Neha", 21, "Mumbai"]
# ]
# #writer.writerows()
# # Writes multiple rows at once
# # writer.writerow()
# # Writes one row at a time


# with open("data.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
#     writer.writerow(["adrika",19,"zirakpur"])

#___________________________________________________________________________________________________________________________#

#Dict reader

# with open("data1.csv","r") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(row)


# writing CSV using Dictionary

# data = [
#     {"name": "Tanishq", "age": 22},
#     {"name": "Adrika", "age": 22}
# ]

# with open("data2.csv", "w", newline="") as f:
#     fieldnames = ["name", "age"]
    
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
    
#     writer.writeheader() 
#     writer.writerows(data)



#common mistakes
# ❌ Not using newline="" while writing
# ❌ Forgetting header in DictWriter
# ❌ Treating all values as int (CSV reads as string)


with open("data2.csv", "r") as f:
        reader = csv.reader(f)
            
        next(reader)  # skip header
            
        with open("output_file", "w") as out:
            for row in reader:
                out.write(row[0] + "\n")  #name column
    