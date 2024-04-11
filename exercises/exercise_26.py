n = int(input("Enter a number: "))
digits = list(str(n))
output = []
for i in range(100,1000):
    dig = list(str(i))
    sum = int(dig[0]) + int(dig[1]) + int(dig[2])
    if sum == n:
        output.append(i)
print(len(output))