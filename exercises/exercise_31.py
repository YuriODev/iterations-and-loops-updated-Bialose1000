n = int(input("Enter the number of days: "))
temps = [int(input("Enter temperature: ")) for _ in range(n)]
print(min(temps))
if min(temps) < -15:
    print("Yes")
else:
    print("No")