favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

team_members = ['anna', 'charles', 'jen', 'sarah', 'edward', 'david', 'phil', 'erin']

for language in sorted(set(favorite_languages.values())):
    print(f"The following language has been mentionned: {language.title()}.")

print("\n")

for member in team_members:
    if member not in favorite_languages.keys():
        print(f"{member.title()}, Please take our poll.")
    else: 
        print(f"Thank you {member.title()} for taking our poll.")


