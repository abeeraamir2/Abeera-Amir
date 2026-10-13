# Break in for loop
for i in range(1, 10):
    if i == 5:
        print("Breaking loop at", i)
        break
    print("Value:", i)

# Break in while loop
x = 0
while x < 10:
    if x == 4:
        break
    print("x is", x)
    x += 1
