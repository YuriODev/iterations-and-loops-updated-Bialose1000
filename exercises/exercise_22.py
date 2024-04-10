n = input("Enter a number: ")
digits = list(n)
for x in range(len(digits), 0, -1):
    print("".join(digits))
    digits.pop(x-1)