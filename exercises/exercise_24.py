n = 1
numbers = []
while n != 0:
    n = int(input("Enter a number: "))
    numbers.append(n)
evenNums = [x for x in numbers if x % 2 == 0]
print(len(evenNums) - 1)