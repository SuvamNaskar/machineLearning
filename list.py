array = [
    ["apple", "banana", "cherry"],
    ["orange", "kiwi", "cherry"],
    ["pineapple", "banana", "cherry"],
    ["grape", "kiwi", "cherry"]
]

for i in array:
    for j in i:
        print(j)

print("\n\n")

array.append(["mango", "chikku", "Strawberry"])
array.insert(3, ["Guava"])

for i in range(0,len(array)):
    for j in range(0,len(array[i])):
        print(array[i][j])
