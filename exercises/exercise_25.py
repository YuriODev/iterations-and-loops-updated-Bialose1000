d = int(input("Input distance: "))
t = int(input("Input target distance: "))
distance = d
days = 1
found = False
while not found:
    distance += d*(1.1**(days))
    if distance > t:
        found = True
    days += 1

print(f"{round(distance,2)} km, {days} days")