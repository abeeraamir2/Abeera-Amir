# User-defined exception
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be 18 or above"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_voting_eligibility(age):
    if age < 18:
        raise InvalidAgeError(age)
    print("Eligible for registration! Age is:", age)

try:
    check_voting_eligibility(20)
    check_voting_eligibility(15)
except InvalidAgeError as e:
    print("Caught custom exception:", e)
