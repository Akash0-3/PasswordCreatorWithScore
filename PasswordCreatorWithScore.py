import string

def createPassword():
    password = input("Enter the password:")

    if len(password) < 8:
        print("Your password is too short! (have minimum 8 characters)\n")
        createPassword()

    if len(password) > 20:
        print('length should be not be greater than 8\n')
        createPassword()
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral\n')
        createPassword()

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter\n')
        createPassword()

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter\n')
        createPassword()
    if not any(char in string.punctuation for char in password):
        print('Password should have at least one of the symbols $@#\n')
        createPassword()
    else:
        print("\nCreated password successfully (with all requirement)\n")
        print("want to know your password score!")
        choice = input("For yes-->(y/y) // For no -->(N/n)")
        if choice == 'y' and 'Y':

            score = 0

            upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
            lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
            special = any([1 if i in string.punctuation else 0 for i in password])
            digits = any([1 if i in string.digits else 0 for i in password])

            char = [upper_case, lower_case, special, digits]

            leng = len(password)

            if leng >= 8:
                score += 1

            if leng >= 10:
                score += 1

            if leng >= 12:
                score += 1
            if leng > 20:
                score += 1

            print(f"password length {str(leng)}, adding score {str(score)}")

            if sum(char) > 1:
                score += 1
            if sum(char) > 2:
                score += 1
            if sum(char) > 3:
                score += 1

            print(f"password has {str(sum(char))} different characters types, adding score {str(score)}")

            if score < 4:
                print(f"\nthe password is quite weak! Score: {str(score)} \n")
            elif score == 4:
                print(f"\nthe password is OK! ! Score: {str(score)} \n")
            elif 4 < score < 6:
                print(f"\nthe password is pretty good! Score: {str(score)} \n")
            elif score >= 6:
                print(f"\nthe password is strong! Score: {str(score)} \n")
        else:
            print("\nThanks!! See you again :) \n")
while True:
    print("Creating a password!!")
    print("1-->To create a password")
    print("2-->Exit")
    user = int(input("Enter a choice:"))

    if user == 1:
        createPassword()
    elif user == 2:
        exit()
    else:
        print("Invalid Try Again!! \n")


