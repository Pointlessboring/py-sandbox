from users_split import Users

class Priviledges:

    def __init__(self) -> None:
        self.priviledges = ["can add post", "can ban user", "can delete post"]

    def show_priviledges(self):
        for priv in self.priviledges:
            print(f"Admins can: {priv}")

class Admin(Users):

    def __init__(self, first_name, last_name, age=None, job=None):
        super().__init__(first_name, last_name, age, job)
        self.admin_priviledges = Priviledges()