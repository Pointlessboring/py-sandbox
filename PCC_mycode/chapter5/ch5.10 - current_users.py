current_users = ['dave', 'zoltan', 'ann', 'michael', 'eric']
new_users = ['charles', 'ben', 'fred', 'zoltan', 'ANN']

for user in new_users:
    if user.lower() in current_users:
        print(f"{user} was already in list of current users.")
    else:
        print(f"Adding {user} to list of current users.")
        current_users.append(user)

print(current_users)
