n = int(input("Enter a number: "))
numbers = [str(x) for x in range(1, n) if list(str(x)) == list(str(x))[::-1]]
print(len(numbers))