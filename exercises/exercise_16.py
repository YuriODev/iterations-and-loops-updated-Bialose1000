n = int(input("Enter a number: "))
num1, num2 = n, 1
output =[]
while num1 > 0:
    space = [" " for _ in range(num1)]
    spaces = "".join(space)
    hash = ["#" for _ in range(num2)]
    hashes = "".join(hash)
    print(spaces + hashes)
    num1 -= 1
    num2 += 1
