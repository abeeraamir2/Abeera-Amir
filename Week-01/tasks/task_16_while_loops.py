# Counter while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Factorial using while loop
num = 5
fact = 1
temp = num
while temp > 1:
    fact *= temp
    temp -= 1
print("Factorial of", num, "is", fact)

# While else
i = 0
while i < 3:
    print("Step:", i)
    i += 1
else:
    print("Loop finished normally")
