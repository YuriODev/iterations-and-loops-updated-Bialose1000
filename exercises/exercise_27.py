def oddNumber(n):
    return int(2*n - 1)

n = int(input("Enter a number: "))
pi = [((4/oddNumber(x))*(-1)**(x+1)) for x in range(1,n+1)]
print(sum(pi))