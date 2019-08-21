# import random module to use later for shuffling deck
import random
# set up global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# values will be a dictionary so we can pass in rank and get the numerical value of it. Important for face cards and ace
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
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)

# Hand class which is basically representation of player, to hold Card objects dealt from Deck class, and also calcualte the value of those cards using above global dictionary
# also adjusts value for Aces when appropriate
class Hand:
  def __init__(self):
    # start with empty list as we did in Deck class
    self.cards = []
    # start with 0 value of the hand
    self.value = 0
    # add attribute to keep track of aces
    self.aces = 0

  # method for adding a card. 'card' param is actually from Deck.deal() which is a single card obj
  def add_card(self,card):
    # grab empty list from __init__ method and append card to it
    self.cards.append(card)
    # since the card from Deck.deal is going to have a rank, we can grab that rank for value's dictionary as the key
    self.value += values[card.rank]

    # track aces
    if card.rank == 'Ace':
      self.aces += 1

  # method to adjust the value of aces
  def adjust_for_ace(self):
    # first check to see if the value is over 21. If it is we will not want to adjust value of ace to 1
    # IF total value is over 21 and We still have an ace left, change that value to be 1 instead of 11
    while self.value > 21 and self.aces:
      # change value from 11 to 1 by sub 10
      self.value -= 10
      # subtract an ace
      self.aces -= 1


# test for Hand class
# test_deck = Deck()
# test_deck.shuffle()
# # create test player
# test_player = Hand()
# # deal one card from deck. Card(suit,rank)
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)

# Chips class to keep track of a player's chips, bets and ongoing winnings
class Chips:
  # total=100 is going to be default amt of chips players start with unless something different is passed
  def __init__(self,total=100):
    self.total = total
    self.bet = 0 

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet

# functions for main game 

# function for taking bets. Take in chips from class above which have total and bet attrs
def take_bet(chips):
  while True:
    try:
      chips.bet = int(input("How many chips would you like to bet? "))
    except:
      print("Sorry, please provide an integer.")
    else:
      if chips.bet > chips.total:
        print(f"Sorry, you don't have enough chips to bet that much. You have {chips.total} chips.")
      else:
        # if an integer was passed and it is less than total, we can break out of While True loop
        break

# function for taking hits. Takes in the deck and a player's hand to add to
# Either player can take hits until they bust
def hit(deck,hand):
  # assign popped card from Deck.deal() to single_card
  single_card = deck.deal()
  # add that card to the hand
  hand.add_card(single_card)
  # call method to check if we need to adjust ace value
  hand.adjust_for_ace()

  # function to ask player if they would like to hit or stand
def hit_or_stand(deck,hand):
  # set global variable to control upcoming while loop
  global playing

  while True:
    x = input("Hit or Stand? Enter H/S ")

    if x[0].lower() == 'h':
      # use hit() from above to hit
      hit(deck,hand)
    elif x[0].lower() == 's':
      print("Player Stands... Dealer's turn")
      playing = False
    else:
      print("Incorrect input... Please enter H or S")
      # use continue to go back to top of loop for another input
      continue
    # if none of these gets triggered we can break out of loop
    break

# functions to display cards
def show_some(player,dealer):
  print("DEALER'S HAND: ")
  print('One card is hidden')
  print(dealer.cards[1])
  print("\n")
  print("PLAYER'S HAND: ")
  for card in player.cards:
    print(card)

def show_all(player,dealer):
  print("DEALER'S HAND: ")
  for card in dealer.cards:
    print(card)
  print("\n")
  print("PLAYER'S HAND: ")
  for card in player.cards:
    print(card)

# functions to handle end of game scenarios. Note player is represented by hand object
def player_busts(chips):
  print("BUST PLAYER!")
  # call lose_bet method from chips class to adjust chips
  chips.lose_bet()

def player_wins(chips):
  print("PLAYER WINS!")
  # call win_bet method from chips class to adjust chips
  chips.win_bet()

def dealer_busts(chips):
  print("DEALER BUSTS! PLAYER WINS!")
  chips.win_bet()

def dealer_wins(chips):
  print("DeALER WINS!")
  chips.lose_bet()

# note push doesn't take in chips because push means both dealer and player got 21 so nothing happens with chips
def push():
  print("Player and Dealer tie! PUSH...")










