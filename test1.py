import csv

with open('data.csv', 'r', encoding='Windows-1251') as f:
    fields = ["ID","Name"]
    reader = csv.DictReader(f, delimiter=';')
    n = 0
    streets = []
    for row in reader:
        #print(row["ID"], "-", row["Name"], row["Street"])
        if row["Pavilion"] == "да":
            streets.append(row["Street"])
        n += 1
    print(n)
    #print(streets)
street_counts =[]
for street in streets:
    street_count = streets.count(street)
    #print(street, street_count)
    street_counts.append(street_count)
max_street_counter = max(street_counts)
index1 = street_counts.index(max_street_counter)
print(streets.pop(index1))