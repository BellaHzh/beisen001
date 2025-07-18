# username = 'jas'
# len(username) --> returns 3

username = input("Enter your username: ")
username_len = len(username)
while username_len <= 5:
    print("Invalid Username! Username should be longer than 5 characters.")
    username = input("Enter your new username: ")
    username_len = len(username)
print("You've registered successfully. Welcome, " + username + "!")
