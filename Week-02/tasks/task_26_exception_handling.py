# Handling ZeroDivisionError
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling ValueError
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid number format!")

try:
    val = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful, result is:", val)
finally:
    print("This block always executes.")
