#Display Art#
from art import logo
from art import vs
from game_data import data
import random
# Formate the account data into printable format
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(user_guess, a_follower_count, b_follower_count):
    """"Check if the user is correct."""
    if a_follower_count > b_follower_count:
        return user_guess == "a" 
    else:
        return user_guess == "b"
    

#Generate random account from the user
account_a = random.choice(data)
account_b = random.choice(data)
#checking if the two accounts are the same
if account_a == account_b:
    account_b = random.choice(data)

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#Make the game repeatable.
print('Before While')
while game_should_continue:
 
    account_a == account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data) 

#Generate a random account from the game data.



    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")


    # Ask the user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #Clear the screen between rounds.
    print("\n" *20)
    


    #Check if user is correct.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)



    #Give user feedback on their guess.
    #score Keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}" )
        print('Welcome to next round')
    else:
        print(f"Sorry, that's wrong. Your score is {score}./n")
        print('Game Over')
        






#Making the acount at the position B  become the  account at position A.