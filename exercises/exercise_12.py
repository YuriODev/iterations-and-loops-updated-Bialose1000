n = int(input("Enter a number: "))
sum, num = 0, 100
while num < 999:
    if num % n == 0:
        sum += num
    num += 1


print(sum)