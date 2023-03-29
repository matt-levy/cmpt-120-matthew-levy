class User:
    def __init__(self, first_name, last_name, userid, email):
        self.first_name = first_name
        self.last_name = last_name
        self.userid = userid
        self.email = email
        self.role = "user"

users = []

def to_string(user):
    return user.first_name + "," + user.last_name + "," + user.userid + "," + user.email

#creates a list of users from txt file, requires an established list
def create_user_list():
    file = open('users.txt', 'r')
    data = file.read()

    for z in data.split('\n'):
        if z:
            user = User(*z.split(','))
            users.append(user)

create_user_list()

for elem in users:
    print(to_string(elem))