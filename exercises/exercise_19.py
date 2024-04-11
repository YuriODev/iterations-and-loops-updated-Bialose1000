n = int(input("Enter a number: "))
numbers = [[x,y] for x in range(1,10) for y in range(10)]
correctNumbers = [x for x in numbers if ((x[0])**2 + (x[1])**2) % n == 0]
output = [str(x[0]) + str(x[1]) for x in correctNumbers]
print(", ".join(output))