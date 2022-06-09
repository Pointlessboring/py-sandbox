#####
# ceasar cracker
# cypher: c = (x + n) % 26

# Step #1: Started from the cypher P6

def main():
    print("Please enter the message to process")
    msg = input('> ')

    for n in range(24):
        print(f"Key #{n}: {crypt(msg, -n)}")

def crypt(text, offset):
    return ''.join([x if (ord(x) not in range(64, 90)) else chr((((ord(x)-64) + offset)%26)+64) for x in text])

# If the program is run (instead of imported), run main():
if __name__ == '__main__':
    main()