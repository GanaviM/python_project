class BasePasswordManager(object):
    old_passwords = ["Python",1236,"ganavi"]                                                                                        
    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password):                            
        return self.get_password() == password                

class PasswordManager(BasePasswordManager):                
                                                           

    def set_password(self, new_password):
        if self.get_level() < self.get_level(new_password) and len(new_password) >= 6:
            self.old_passwords.append(new_password)
            print("Password changed Successfully.")
        else:
            print("Password not changed. Please use a stronger password")

    def get_level(self, password = None):     
        if password == None:
            password = self.get_password()

        if password.isalpha() or password.isnumeric():
            level = 0
        elif password.isalnum():
            level = 1
        else:
            level = 2
        return level


Pass= BasePasswordManager()
new_pass = input("Enter new Password: ")
print(f"Is current password same as a new password: {Pass.is_correct(new_pass)}")

manage= PasswordManager()
manage.set_password(new_pass)
print(f"Security Level of Password: {manage.get_level()}")
