n1 = input("Enter a number: ")
n2 = input("Enter the search number: ")
if list(str(n1)).count(n2) > 0:
    print(list(n1)[::-1].index(n2) + 1)
else:
    print(0)