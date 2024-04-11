n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
numbers = [str(x) for x in range(n1 + (n1 % 2), n2, 2)]
print(" ".join(numbers))