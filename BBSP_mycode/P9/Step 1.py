# Collatz conjecture
# https://en.wikipedia.org/wiki/Collatz_conjecture


def main():

    while True:
        print('what is the starting number? ')
        response = input('> ')
        if response.isdecimal():
            break  # User has entered a valid amount.

    collatz(int(response))

def collatz (n):
    print(f"{n} ", end='')
    if n != 1: 
        return collatz(int(n/2 if (n%2 == 0) else (3 * n + 1)))

# If this program was run (instead of imported), run main():
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('=- Collatz conjecture -=, by @PointlessBoring')