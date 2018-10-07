from random import randint
import json

class deckOfCards:
    # TODO load these from a file or somewhere
    suits = ['♠', '♣', '♥', '♦']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_string = None

    deck = []

    def __init__(self):
        with open("settings.json", encoding="utf-8") as json_file: 
            settings = json.loads(json_file.read())
        self.suits = settings['suits']
        self.cards = settings['cards']
        self.card_string = settings['cardString']
        # We don't need to explicitly create a new deck, since the shuffle method does it for
        self.shuffle()

    def newDeck(self):
        """Returns a new deck, 2-Ace, spades-diamonds"""
        temp_deck = []
        for card in self.cards:
            for suit in self.suits:
                temp_deck.append(self.card_string.format(card, suit))
        return temp_deck

    def shuffle(self, newDeck=True):
        """Randomizes the order of the deck."""
        if newDeck:
            old_deck = self.newDeck()
        else:
            old_deck = self.deck[:]
        self.deck = []
        while len(old_deck) > 0:
            self.deck.append(old_deck.pop(randint(0, len(old_deck) - 1)))
        
    def cut(self):
        cut_spot = randint(1, len(self.deck) - 2)
        self.deck = self.deck[cut_spot:] + self.deck[:cut_spot]

    def dealOneCard(self):
        """Deals and returns one card from the top of the deck. The end of the list is considered the top."""
        if (len(self.deck) <= 0):
            return None
        return self.deck.pop()

if __name__ == '__main__': # Draw poker for testing
    the_deck = deckOfCards()
    hand = []
    keep_playing = True
    while keep_playing:
        for i in range(0, 5): # Poker hand of 5 cards
            hand.append(the_deck.dealOneCard())
        print(str(hand))
        valid_input = False
        while not valid_input:
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
                    print("Invalid input. Try again.")

        while len(final_hand) < 5:
            final_hand.append(the_deck.dealOneCard())
        
        print(final_hand)
        valid_input = False
        while not valid_input:
            print("Would you like to play again? (y/n)")
            play_again = input()
            if play_again.lower() == "y":
                valid_input = True
                keep_playing = True
            elif play_again.lower() == "n":
                valid_input = True
                keep_playing = False
            else:
                print("That was not a valid input.")