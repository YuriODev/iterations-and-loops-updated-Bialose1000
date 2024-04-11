n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
numbers = [str(x) for x in range(n1, n2) if list(str(x)) == list(str(x))[::-1]]
print(" ".join(numbers))