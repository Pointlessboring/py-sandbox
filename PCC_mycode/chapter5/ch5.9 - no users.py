users = ['admin', 'marc', 'andre', 'steve', 'eric', 'ann']

users.sort(reverse=True)

print(f"We have {len(users)} users.")

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else: 
    print("We need to find some users!")

print("\n")

for n in range(0, len(users)):
    print(f"Removing user: {users.pop()}")

print("\n")
print(f"We have {len(users)} users.")

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else: 
    print("We need to find some users!")