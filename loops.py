x = 5
while x > 0:
    print(f"hello {x}")
else:
    print("bye")

while (x > 0):
    print(f"hello {x}")
    if x == 2:
        break
    x -= 1
else:
    print("bye")