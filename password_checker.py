# write a code for enter strengthen password from user

password = input("Enter password: ")
while True:
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Password must include an uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Password must include a lowercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Password must include a digit.")
    elif not any(char in "@#$%^&*" for char in password):
        print("Password must include a special character.")
    else:
        break
    password = input("Enter a strong password: ")

print("Password is strong.")