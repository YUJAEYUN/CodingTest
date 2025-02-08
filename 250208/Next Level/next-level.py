user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!
class user:
    def __init__(self, user_id='codetree', user_level=10):
        self.user_id = user_id
        self.user_level = user_level

user2 = user()
print("user",user2.user_id,"lv",user2.user_level)
user2.user_id = user2_id
user2.user_level = user2_level

print("user",user2.user_id , "lv",user2.user_level)