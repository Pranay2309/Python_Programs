w = int(input("Enter number of waves: "))

for y in range(0, w):
    print(end="    ")
    print("*",end=" ")
print()

for y in range(0, w):
    print(end="   ")
    print("*", end = "")
    print(end=" ")
    print("*", end = "")
print()

print(end=" ")
for y in range(0, w):
    print(end=" ")
    print("*", end="   ")
    print("*", end = "")
print()

for y in range(0, w+1):
    print(end=" ")
    print("*", end = "    ")
