invitees = ["Jiddu Krisnamurti", "Steve Jobs", "Albert Einstein", 
           "Isaac Newton", "JS Bach", "William Shakespeare", "Winston Churchill"] 

print(f"Unfortunately, {invitees[0].title()}, can't make it to dinner.")
del invitees[0]

print(f"Dear {invitees[0].title()}, you are invited to dinner.")
print(f"Dear {invitees[1].title()}, you are invited to dinner.")
print(f"Dear {invitees[2].title()}, you are invited to dinner.")

print("\nEveryone, we now have a bigger table, so we can invite more guests\n")

revised_invitees = []
revised_invitees.append(invitees[0].title())
revised_invitees.append(invitees[1].title())
revised_invitees.append(invitees[2].title())

revised_invitees.insert(0,invitees[-1])
revised_invitees.insert(2,invitees[-2])
revised_invitees.append(invitees[-3])
print(revised_invitees)


print(f"Dear {revised_invitees[0].title()}, you are invited to dinner.")
print(f"Dear {revised_invitees[1].title()}, you are invited to dinner.")
print(f"Dear {revised_invitees[2].title()}, you are invited to dinner.")
print(f"Dear {revised_invitees[3].title()}, you are invited to dinner.")
print(f"Dear {revised_invitees[4].title()}, you are invited to dinner.")

print("\n")