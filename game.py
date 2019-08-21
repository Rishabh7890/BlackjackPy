# import random module to use later for shuffling deck
import random
# set up global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
# declare boolean value to control while loops for game
playing = True

# create a card class
class Card:
  
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f'{self.rank} of {self.suit}'

# create a deck class to hold our 52 card objects in a list
class Deck:

  def __init__(self):
    # start with an empty list
    # this deck attribute is not taken into the __init__ method because we want the deck to be standard everytime
    self.deck = []
    # nested loop to get every card and then append as tuple to self.deck using Card class and pass in suit and rank as params
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))
  
  def __str__(self):
    deck_composition = ''
    # for loop to print out string representation of each card from Card's __str__ method
    for card in self.deck:
      deck_composition += '\n' + card.__str__()
    return 'The deck has: ' + deck_composition

  # method to shuffle the deck
  def shuffle(self):
    # note no return statement because we are just shuffling the deck in place
    random.shuffle(self.deck)

  # deal method to actually grab a card from the self.deck attr
  def deal(self):
    # grab the deck attr of the deck class and pop off last item on the list to save it to single_card
    single_card = self.deck.pop()
    # return the single popped off card as card to deal
    return single_card

# test to see if Card and Deck classes work
test_deck = Deck()
test_deck.shuffle()
print(test_deck)



