import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try: 
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_username():
    """Prompt for a new username."""
    return input("What is your name? ")

def get_new_username(username):
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username    

def greet_user():
    """Greet the user by name."""
    current_user = get_username()
    username = get_stored_username()
    if username == current_user:
        print(f"Welcome back, {username}!")
    else: 
        username = get_new_username(current_user)
        print(f"We'll remember you when you come, back {username}!")

greet_user()