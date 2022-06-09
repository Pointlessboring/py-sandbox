#####
# ceasar cypher: c = (x + n) % 26

# Step #1: Basic structure
# Step #2: User interaction
# Step #3: Fixed the space problem.
# Step #4: Combine encrypt/decrypt functions.

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
    msg = input('> ')

    if action == 'd':
        key *= -1
    print(crypt(msg, key))

def crypt(text, offset):
    return ''.join([x if (ord(x) not in range(64, 90)) else chr((((ord(x)-64) + offset)%26)+64) for x in text])

# If the program is run (instead of imported), run main():
if __name__ == '__main__':
    main()