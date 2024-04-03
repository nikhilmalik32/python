import string
import getpass

# It is used to take the password input from the user 
def check_password_strength():
    password = getpass.getpass('Enter the password: ')
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0
# It is the for loop to iterate to each characters  in password
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1
# To increment the value of strength 
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
# To tell the user how strong the password has been made
    if strength == 1:
        remarks = ('That\'s a very bad password.'
                   ' Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a weak password.'
                   ' You should consider using a tougher password.')
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = ('Your password is hard to guess.'
                   ' But you could make it even more secure.')
    elif strength == 5:
        remarks = ('Now that\'s one hell of a strong password!!!'' Hackers don\'t have a chance guessing that password!')
# To display how many upper case letters,lower case letters ,special symbols,whitespaces has been used and
# to display the strength of the password out of 1
    print('Your password has:-')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{num_count} digits')
    print(f'{wspace_count} whitespaces')
    print(f'{special_count} special characters')
    print(f'Password Score: {strength / 5}')
    print(f'Remarks: {remarks}')
# To iterate the loop after the password has been entered by user is valid or not and after entering the password 
# if the password is correct it will ask for another password

def check_pwd(another_pw=False):
    while True:
        if another_pw:
            choice = input('Do you want to check another password\'s strength (y/n) : ')
        else:
            choice = input('Do you want to check your password\'s strength (y/n) : ')

        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Exiting...')
            return False
        else:
            print('Invalid input...please try again.\n')

# To check whether the code is imported as module or runs directly
if __name__ == '_main_':
    print('===== Welcome to Password Strength Checker =====')
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)