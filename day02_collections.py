#---------------------------------
# Day 2: Collections
#---------------------------------


# List: ordered, allows duplicates
nums = [1, 2, 3, 3]
nums.append(4)
print("list:", nums, "first:", nums[0], "last:", nums[-1])

# Set: unique values only (great for dedupe and fast membership tests)
unique = set(nums)
print("unique set:", unique, "contains 3?", 3 in unique)

# Dictionary: key-value pairs (like JSON)
# Dict: key-value store (hash map)
person = {"name": "Sal", "city": "Vegas"}
person["age"] = 50  # add new key
print("dict:", person, "name value:", person["name"])

# Tuple: immutable grouping
point = (10, 20)
print("tuple:", point)

# JSON: write/read a Python object as text
import json
with open("tasks.json", "w") as f:
    json.dump({"tasks": [{"title": "Finish Day 2", "isDone": False}]}, f)

with open("tasks.json") as f:
    data = json.load(f)
print("loaded json:", data)

# CSV: write/read tabular data
import csv
with open("tasks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "isDone"])
    writer.writerow(["Finish Day 2", False])
    writer.writerow(["Start Day 3", False])

with open("tasks.csv") as f:
    reader = csv.DictReader(f)  # gives dicts per row using header names
    rows = list(reader)
    print("csv rows:", rows)
