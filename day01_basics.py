#variables
x = 5
y = 3.14
name = "Sal"
is_done = True
print(x, y, name, is_done)

#Lists
nums = [1, 2, 3, 4, 5]
nums.append(6)
print("First number:", nums[0], "Last number:", nums[-1])

#Dictionaries
person = {"name": "Sal", "agePreference": "Getting older"}
person ["age"] = 30
print(person)

#loops
for n in [1, 2, 3]:
    print(n)

count = 0
while count < 3:
    print("Count is:", count)
    count += 1

#functions
def square(num):
    return num * num
print("Square of 4 is:", square(4))


