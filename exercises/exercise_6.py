num = int(input("Enter a number: "))
n = 1
while n < num + 1:
    output = ["*" for _ in range (n)]
    print("".join(output))
    n += 1