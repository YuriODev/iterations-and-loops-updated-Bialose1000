n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
numbers = [str(x) for x in range(n1, n2)]
output = []
for num in numbers:
    numb = list(num)
    for e in range(0,9):
        if numb.count(str(e)) == 3:
            output.append(num)

print(" ".join(output))