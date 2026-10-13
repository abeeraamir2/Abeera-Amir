# Continue in for loop to print only odd numbers
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# Continue with strings
word = "Python"
for letter in word:
    if letter == "o":
        continue
    print("Letter:", letter)
