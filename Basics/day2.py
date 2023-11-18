
# Welcome to the Tip Calculator
print("Welcome to the Tip Calculator.")
amt = int(input('What was the total bill?'))
tip = int(input("What percentage of tip would you like to give?"))
split_in = int(input('How many people to split the bill?'))

total_bill = amt + amt * (tip/100)
splitted_bill = round((total_bill/split_in),2)
print(f"Each person should pay: ${splitted_bill}")

#If the bill was 