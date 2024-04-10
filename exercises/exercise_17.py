rows = int(input("Enter the first number: "))
columns = int(input("Enter the second number: "))
numbers = [[] for _ in range(rows)]
for x in range(rows):
    for y in range(columns):
        numbers[x].append(str(x))
print(numbers)
for i in range(len(numbers)):
    print("      ".join(numbers[i]))
