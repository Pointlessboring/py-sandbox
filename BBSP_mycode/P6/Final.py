#####
# ceasar cypher: c = ((x + n - 1) % 26) + 1

# Step #1: Basic structure
# Step #2: User interaction
# Step #3: Fixed the space problem.
# Step #4: Combine encrypt/decrypt functions.
# Step #5: Simplify the encrytpion function by validating inputs before.

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

    msg = ""
    while msg == "":
        print("Please enter the message to process (Letters only)")
        msg = input('> ').upper()       # upper() ensure ord will be between 65 and 90
        if not msg.isalpha():           # validate that only letters are entered.
            print("Letters only please!")
            msg = ""

    if action == 'd':
        key *= -1                       # Encrypt offset positively, Decrypt negatively.
    print(crypt(msg, key))

def crypt(text, offset):
    """ This function offsets the letters by a certain number of characters. """
    """ ord(x) returns the ASCII code. """
    """ subtract 64 to get the letter number subtrack 1 apply modulo 26 """
    """ then add 64 + 1 back for the ASCII Code. """

    """ See excel worksheet to understand the modulo function """

    return ''.join( [ chr((((ord(x)-64) + offset - 1 )%26) + 64 + 1 ) for x in text] )

# If the program is run (instead of imported), run main():
if __name__ == '__main__':
    main()