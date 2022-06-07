class Users:

    def __init__(self, first_name, last_name, age=None, job=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        print(f"Here is the information we have on this user:")
        print(f"- First name: {self.first_name}")
        print(f"- Last name: {self.last_name}")
        
        if self.age != None:
            print(f"- Age: {self.age}")
        
        if self.job != None:
            print(f"- Job: {self.job}")
        
    def greet_user(self):
        print(f"Greetings, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Increment login attemps counter when a login fails"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset counter to zero after a successful login"""
        self.login_attempts = 0

user1 = Users('joe', 'laviolette', 12, 'analyst')
user2 = Users('mary', 'poppins', job='teacher')
user3 = Users('tom', 'jones', 67, 'singer')

print("\n")
user1.greet_user()
user1.describe_user()
    
print("\n")
user2.greet_user()
user2.describe_user()

print("\n")
user3.greet_user()
user3.describe_user()

# Ex9.5 added login attempts
print("\n")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"{user1.first_name.title()} {user1.last_name.title()} has failed to login {user1.login_attempts} times.")

user1.reset_login_attempts()
print(f"{user1.first_name.title()} {user1.last_name.title()} has failed to login {user1.login_attempts} times.")