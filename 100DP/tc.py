try:
    age = int(input('How old are you?'))
except ValueError:
    print('Invalid input. Please enter a numeric value.')
    age = int(input('How old are you?'))
if age > 18:
    print(f'You can drive at {age}.')
else:
    print('You cannot drive at {age}.')