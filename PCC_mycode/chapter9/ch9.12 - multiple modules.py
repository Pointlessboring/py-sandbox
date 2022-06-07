from admin_split import Admin, Users
    
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
