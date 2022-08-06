names = ["TomTom", "Hershey", "Caramel", "Cookie"]
names[0] = "Tomtom"
print(names[0:3])
print(names)

names.append("Candy")
print(names)

names.insert(1, "Cream")
print(names)

# names.clear()
# print(names)

print("Candy" in names)
print(len(names))

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1