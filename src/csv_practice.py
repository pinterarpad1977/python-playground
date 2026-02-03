import csv

older_than_30 = []

with open("/app/data/people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(f"{row['name']} is {row['age']} years old and lives in {row['city']}")
        age = int(row["age"])
        if age > 30:
            older_than_30.append(row)

with open("/app/data/older_than_30.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames= fieldnames)

    writer.writeheader()
    writer.writerows(older_than_30)
    
