n = 1
numbers = []
while n != 0:
    n = int(input("Enter number: "))
    numbers.append(n)
print
print(sum(numbers) / (len(numbers) - 1))