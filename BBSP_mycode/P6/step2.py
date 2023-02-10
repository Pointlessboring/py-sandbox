#####
# ceasar cypher: c = (x + n) % 26


# Step #1: Basic structure
# Step #2: User interaction

def main():

    action = 'x'
    while action not in 'de':
        print("Do you want to (e)ncrypt or (d)ecrypt? ")
        action = input('> ')

    key = 0
    while key == 0:
        print("Please enter the key to use (0 to 25) ")
        key = input('> ')
        if not key.isdecimal():
            key = 0
    key = int(key)
    print("Please enter the message to process")
    msg = input('> ').upper()

    if action == 'd':
        print(decrypt(msg, key))
    else:
        print(encrypt(msg, key))


def encrypt(text, offset):
    return ''.join([chr( (((ord(x)-64) + offset)%26)+64) for x in text])

def decrypt(text, offset):
    return ''.join([chr( (((ord(x)-64) - offset)%26)+64) for x in text])

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()