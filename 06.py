import random
def generate_random_number(start, end):
    return random.randint(start, end)
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

random_number = generate_random_number(start, end)

print(f"The random number between {start} and {end} is: {random_number}")

