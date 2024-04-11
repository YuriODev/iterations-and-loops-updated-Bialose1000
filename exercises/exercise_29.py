numbers = list()
started = "n"
while sum(numbers) != 0 or started == "n":
    n = int(input("Enter a number: ")) 
    numbers.append(n)
    started = "y"

output = 0
for x in numbers:
    output += x**2

print(output)