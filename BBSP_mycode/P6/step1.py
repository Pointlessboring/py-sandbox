#####
# ceasar cypher: c = (x + n) % 26


# Step #1: Basic structure

def main():

    # action = input("Do you want to (e)ncrypt or (d)ecrypt? ")

    test = 'Meet me by the rose bushes tonight'.upper()

    test1 = encrypt(test, 4)
    print(test1)
    pass


def encrypt(text, offset):
    return ''.join([chr( (((ord(x)-64) + offset)%26)+64) for x in text])

def decrypt(text, offset):
    return ''.join([chr( (((ord(x)-64) - offset)%26)+64) for x in text])

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()