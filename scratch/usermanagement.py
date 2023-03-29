from user import User
from user import create_user_list

users = []

create_user_list()

#converts user object to string
def to_string(user):
    return user.first_name + "," + user.last_name + "," + user.userid + "," + user.email

#prints first and last names of all users in list
def print_names(list):
    for user in list:
        print(user.first_name + " " + user.last_name)

#removes user from txt file
def remove_user(user):
    #reads txt file and stores data in lines
    file = open("users.txt", "r")
    lines = file.readlines()
    file.close()
    #iterates through lines to print all except chosen user
    file = open("users.txt", "w")
    for line in lines:
        if line.strip("\n") != to_string(user):
            file.write(line)
    file.close()
    
#adds user to the end of the txt file
def add_user(user):
    file = open('users.txt', 'a')
    file.write("\n" + to_string(user))
    file.close()

bob = User("Bob", "Dylan", "bd123", "bd123@fakemail.com")

#print_names(users)
#add_user(bob)
#remove_user(bob)