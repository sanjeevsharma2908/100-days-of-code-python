# Roller coaster Ride programme
print("Welcome to the Rollercoaster!")
height = int(input('What is your height in CM? '))
total_bill = 0

if height >=120:
    print ("You are a tall person. You will be able to ride on all roller coasters!")
    age = int(input('What is your age? '))
    if age < 12:
        total_bill = 5
        print('Child tickets are $5.')
    elif age <= 18:
        total_bill = 7
        print('Youth tickets are $7.')
    else:
        total_bill = 12;
    print('Adults tickets are $12.')
    wants_photos = input('Do you want a photo taken ? Y or N. ')
    if wants_photos == "Y":
        total_bill +=3
    print(f"Your final bill is ${total_bill}")
    print('Have a Safe and Secure ride wooooh!')
else:
    print("Sorry, You have to grow before you can ride.")