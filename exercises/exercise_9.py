n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))
n3 = int(input("Enter third number :"))
output = [str(x) for x in range(n1,n2 + 1) if x % n3 == 0]
print(" ".join(output))