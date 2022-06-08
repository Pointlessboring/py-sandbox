# Step 1: Basic Deck information and card printing.
# Step 2: Main game loop. Get bet function.
# Step 3: Get_deck function, shuffle, pick and display hands.
# Step 4: Calculate card value
# Step 5: Player actions
# Step 6: Dealer action

import random, sys

from matplotlib.pyplot import pause

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
SUIT     = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
BACKSIDE = 'backside'

def main():
    """This is a simple blackjack application."""
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

        # Player action
        
        while True:

            displayHands(player_hand, dealer_hand, False)
            player_choice = get_move(player_hand)

            if player_choice == 'S':
                break
            elif player_choice == 'D':
                extra_bet = get_bet(min(money-bet, bet))
                bet += extra_bet
            player_hand.append(deck.pop())

        if getCardValue(player_hand) < 21:
            # Dealer action
            while getCardValue(dealer_hand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                displayHands(player_hand, dealer_hand, True)
        else: 
            # Player has busted
            print("You lose")
            money -= bet
            break

        print("\n")

     
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
            bet = 0
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

def displayHands(player_hand, dealer_hand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""
    
    print()
    if showDealerHand:
        print('DEALER:', getCardValue(dealer_hand))
        displayCards(dealer_hand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealer_hand[1:])

    # Show the player's cards:
    print('PLAYER:', getCardValue(player_hand))
    displayCards(player_hand)

def getCardValue(cards):
    """Calculate the value of a given hand."""

    value = 0
    aces  = 0

    for rank, suit in cards:
        if rank in ['10', 'J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 1
            aces += 1
        else: 
            value += int(rank)
    
    while aces > 0:
        if value < 12:
            value += 10
        aces -= 1

    return value

def get_move(player_hand):

    moves = "(S)tand, (H)it"
    if len(player_hand) == 2:
        moves += ", (D)ouble down"
    
    choice = 'X'
    while choice not in moves:
        choice = input(moves+"? ")[0].upper()
    return choice

    


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
