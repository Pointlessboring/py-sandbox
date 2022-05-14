class Priviledges:

    def __init__(self) -> None:
        self.priviledges = ["can add post", "can ban user", "can delete post"]

    def show_priviledges(self):
        for priv in self.priviledges:
            print(f"Admins can: {priv}")

class Users:

    def __init__(self, first_name, last_name, age=None, job=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

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

class Admin(Users):

    def __init__(self, first_name, last_name, age=None, job=None):
        super().__init__(first_name, last_name, age, job)
        self.admin_priviledges = Priviledges()
    
admin1 = Admin('joe', 'laviolette', 12, 'analyst')
user2 = Users('mary', 'poppins', job='teacher')
user3 = Users('tom', 'jones', 67, 'singer')

print("\n")
admin1.greet_user()
admin1.describe_user()
admin1.admin_priviledges.show_priviledges()

print("\n")
user2.greet_user()
user2.describe_user()

print("\n")
user3.greet_user()
user3.describe_user()
