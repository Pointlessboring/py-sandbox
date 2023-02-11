#####
# ceasar cracker
# ceasar cypher: c = ((x + n - 1) % 26) + 1

# Step #1: Started from the cypher P6

def main():
    print("Please enter the message to process")
    msg = input('> ').upper()

    for n in range(24):
        print(f"Key #{n}: {crypt(msg, -n)}")

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