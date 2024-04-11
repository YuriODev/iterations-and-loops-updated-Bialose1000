password = int(input("Password: "))
good =  False
while not good:
    attempt = int(input("Enter Password: "))
    if attempt == password:
        good = True
    else:
        print("Error")
print("Done")