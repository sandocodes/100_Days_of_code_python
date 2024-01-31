# Creating Class

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, "jarso")
user_2 = User(2, "james")
user_3 = User(3, "sando")

# user1 decides to follow user2
user_1.follow(user_2)  # user1 follows user2
user_1.follow(user_3)  # user1 also follows user3

# output user1 following and followers
print(f"{user_1.username.title()} has {user_1.followers} followers")  # expecting 0
print(
    f"{user_1.username.title()} is following {user_1.following} users.")  # expecting 2: User 1 is following 2 accounts (user_2 and user_3)

# User 2 & 3 Followers Fount
print(user_2.followers)  # expecting 1: User_2 is followed by one account (user_1)
print(user_3.followers)  # expecting 1: User_3 followed by one account (user_1)

# Day 17 Completed!
