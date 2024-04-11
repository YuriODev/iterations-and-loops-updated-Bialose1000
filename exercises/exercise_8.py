n = int(input("Enter a number: "))
output = [str(x) for x in range(1,n + 1) if x % 2 == 0]
print(" ".join(output))