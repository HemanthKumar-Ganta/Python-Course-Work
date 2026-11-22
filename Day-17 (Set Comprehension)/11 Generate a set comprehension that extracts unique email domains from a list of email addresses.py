l = ["user1@gmail.com", "user2@yahoo.com", "user3@gmail.com", "user4@outlook.com"]
s = {i.split("@")[1] for i in l }
print(s)