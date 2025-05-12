# list comprehension
# list
# range
# string
# tuple all these are called sequences in python and they are mutable we can easily use list comprehension
import random

indian_names = ["Aarav", "Arjun", "Dhruv", "Ishaan", "Krishna", "Rohan", "Vihaan", "Aanya", "Diya", "Isha",
                "Kavya", "Mira", "Priya", "Riya", "Zara", "Advait", "Kabir", "Reyansh", "Shaurya", "Vivaan"]

random_names = [random.choice(indian_names) for _ in range(10)]
print(random_names)
