def factorial(num):
    sum = 1
    for x in range(1, num + 1):
        sum *= x
    return sum

n = int(input("Enter the limit: "))
numbers = []
for x in range(1, n + 1):
    num = factorial(x)
    numbers.append(num)
print(sum(numbers))