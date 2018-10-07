from random import randint

class deckOfCards:
    # TODO load these from a file or somewhere
    suits = ['♠', '♣', '♥', '♦']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = []

    def __init__(self):
        # We don't need to explicitly create a new deck, since the shuffle method does it for now
        self.shuffle()

    def newDeck(self):
        """Returns a new deck, 2-Ace, spades-diamonds"""
        temp_deck = []
        for card in self.cards:
            for suit in self.suits:
                temp_deck.append("{} {}".format(card, suit))
        return temp_deck

    def shuffle(self):
        # TODO option to shuffle only unused cards
        """Randomizes the order of the deck."""
        old_deck = self.newDeck()
        self.deck = []
        while len(old_deck) > 0:
            self.deck.append(old_deck.pop(randint(0, len(old_deck) - 1)))

    def dealOneCard(self):
        """Deals and returns one card from the top of the deck. The end of the list is considered the top."""
        if (len(self.deck) <= 0):
            return None
        return self.deck.pop()

if __name__ == '__main__': # Draw poker for testing
    the_deck = deckOfCards()
    hand = []
    for i in range(0, 5): # Poker hand of 5 cards
        hand.append(the_deck.dealOneCard())
    print(str(hand))
    print("Which cards would you like to keep?")
    nums = input()
    final_hand = []
    for num in nums: # TODO validate that there are no duplicates and no more than 5 numbers
        try:
            num = int(num)
            if (num > 5):
                raise Exception
            final_hand.append(hand[num - 1]) # 1 index because humans like that
        except:
            print("Invalid input. Quitting")
            raise

    while len(final_hand) < 5:
        final_hand.append(the_deck.dealOneCard())
    
    print(final_hand)