import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

# API → JSON File
with open("users.json", "w") as f:
    json.dump(data, f, indent=4)


# API → TXT File
with open("users.txt","w") as f:
    for user in data:
        f.write(user["name"] + "\n")


# API → CSV File
with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    writer.writerow(["ID", "Name", "Email"])  
    
    for user in data:
        writer.writerow([user["id"], user["name"], user["email"]])


# Q API → Python → Filter → Save CSV

# Step 1: Fetch data from API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# Step 2: Filter data
filtered_data = []

for user in data:
    filtered_data.append({
        "name": user["name"],
        "email": user["email"]
    })

# Step 3: Save to CSV
with open("filtered_users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "email"])
    
    writer.writeheader()
    writer.writerows(filtered_data)

print("Filtered data saved to CSV")