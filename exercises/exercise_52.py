n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
numbers = [str(x) for x in range(n1 - ((n1 - 1) % 2), n2 - 1, -2)]
print(" ".join(numbers))