class User:

    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        """Will be tracking the number of the followers"""
        user.followers += 1
        self.following += 1

user_1 = User('001','sanjeev sharma')
user_2 = User(user_1.id,'Rajeev Sharma')
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)


