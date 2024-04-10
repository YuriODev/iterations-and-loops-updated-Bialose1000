n = int(input("Enter number of numbers being entered: "))
numbers = []
for _ in range(n):
    enter = int(input("Enter a number: "))
    numbers.append(enter)
print(numbers.count(0))