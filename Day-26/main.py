# list comprehension
# list
# range
# string
# tuple all these are called sequences in python and they are mutable we can easily use list comprehension
# import random
#
# indian_names = ["Aarav", "Arjun", "Dhruv", "Ishaan", "Krishna", "Rohan", "Vihaan", "Aanya", "Diya", "Isha",
#                 "Kavya", "Mira", "Priya", "Riya", "Zara", "Advait", "Kabir", "Reyansh", "Shaurya", "Vivaan"]
#
# random_names = [random.choice(indian_names) for _ in range(10)]
# print(random_names)

student_dict = {
    "student": ["sanjeev","Rajeev","kapil"],
    "score": [90,80,70]
}
#Loopinf through dictionaries:
# for (key,value) in student_dict.items():
#     print(f"{key} : {value}")
import pandas
student_data_frame = pandas.DataFrame(student_dict)
assert isinstance(student_data_frame, object)
print(student_data_frame)


# loop through data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through the rows of the data frame

for (index, row) in student_data_frame.iterrows():
    print(row.score)