# Simple function with default argument
def greet(name, course="AI/ML"):
    print(f"Hello {name}, welcome to {course}!")

greet("Ali")
greet("Sara", "Data Science")

# Function returning multiple values
def get_rectangle_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

a, p = get_rectangle_area_and_perimeter(5, 3)
print("Area:", a, "Perimeter:", p)

# Variable-length arguments *args and **kwargs
def calculate_sum(*numbers):
    return sum(numbers)

print("Sum of numbers:", calculate_sum(10, 20, 30, 40))

def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(name="Zain", age=21, grade="A")

# Lambda function
square = lambda x: x * x
print("Square of 5:", square(5))
