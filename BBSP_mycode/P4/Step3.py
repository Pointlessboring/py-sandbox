# Step 1: Basic Deck information and card printing.
# Step 2: Main game loop. Get bet function.
# Step 3: Get_deck function, shuffle, pick and display hands.

import random, sys

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
SUIT     = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
BACKSIDE = 'backside'

def main():

    money = 5000

    while money > 0: 
        print(f"\nYou currently have: {money}")
        bet = get_bet(money)

        # Create a deck, then suffle it
        deck = get_deck()
        random.shuffle(deck)

        # Deal cards to player and dealer.

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Display cards
        
        print("\nDealer: ")
        displayCards(dealer_hand)
        
        print("Player: ")
        displayCards(player_hand)
        print("\n")

        print(bet)
        money -= bet
    
    print("Thank you for playing!")
    
def get_bet(money):
    """Get bet from player or QUIT the program."""
    print("How much do you want to bet? ")
    bet = 0
    while bet == 0:
        bet = input("> ").upper().strip()

        if bet == "QUIT":
            print("Thank you!")
            sys.exit()
    
        if not bet.isdecimal():
            print("Please enter 'QUIT' or a number")
        elif int(bet) > money:
            print(f"You only have {money}. Please bet accordingly.")
            bet = 0
    return int(bet)

def get_deck():
    """Create a new unshuffled deck of cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in SUIT:
            deck.append( (rank, suit) )
    return deck

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '']  # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card.
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
