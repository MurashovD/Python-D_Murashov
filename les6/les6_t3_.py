import pickle
users = {}
user_file = open("t3/users.csv", "r", encoding="utf-8")
hobby_file = open("t3/hobby.csv", "r", encoding="utf-8")
for i in range(2):
    user = user_file.readline().split(",")
    user = user[0] + " " + user[1] + " " + user[2]
    hobby = hobby_file.readline()
    if hobby == "":
        hobby = None
    users[user] = hobby
with open("t3/users.pk", 'wb') as fi:
    pickle.dump(users, fi)
fi.close()
user_file.close()
hobby_file.close()
