num = int(input("Enter a number: "))
n = 1
while n < num + 1:
    output = [" " for _ in range(n-1)]
    print("#" + "".join(output) + "#")
    n += 1