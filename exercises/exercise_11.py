n = int(input("Enter a number: "))
sum, num = 0, 1
while num < n + 1:
    sum += num/(num+1)
    num += 1
print(round(sum,3))