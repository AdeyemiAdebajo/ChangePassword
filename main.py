import os; os.system("cls")
import pyinputplus as pyip
import re
# @Author: Adeyemi Adebajo

class PasswordManager:
    # old_passwords is a list of old passwords
    def __init__(self, old_passwords):
        self.old_passwords = old_passwords
    
    # get the last password in the list
    def get_password(self):
        return self.old_passwords[-1]
    
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        else:
            print('Password already exists')
            return False

    def is_correct(self, password):
        return password == self.old_passwords[-1]

    def validate_password_length(self, password):
        if len(password) < 8:
            print('Password must be at least 8 characters long')
            return False
        return True
        
    def validate_password_characters(self, password):
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$')
        if not password_pattern.match(password):
            print('Password must contain at least one uppercase letter, one lowercase letter, and one special character')
            return False
        return True
    
    def confirm_password(self, new_password, confirm_password):
        return new_password == confirm_password
    
#------------------------------------------------

old_passwords = ['Hello12$', 'Hello123$', 'Hello1234$']
user = PasswordManager(old_passwords)
print(f'Current password: {user.get_password()}')

password_set = False
while not password_set:
    new_password = pyip.inputPassword('Enter new password: ')
    if not user.validate_password_length(new_password):
        continue
    if not user.validate_password_characters(new_password):
        continue
    if user.set_password(new_password):
        while True:
            confirm_password = pyip.inputPassword('Confirm new password: ')
            if user.confirm_password(new_password, confirm_password):
                print('Password changed successfully')
                password_set = True
                break
            else:
                print('Passwords do not match. Please try again.')

print(f'Here are all the passwords: {user.old_passwords}')