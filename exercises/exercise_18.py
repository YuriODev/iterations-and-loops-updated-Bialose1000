n = int(input("Enter the number of days: "))
errors = [int(input("Enter error: ")) for _ in range(n)]
print(sum(errors))