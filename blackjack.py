import random
still_playing = True
#class constructor for cards
class card:
    def __init__(self, suit, card_name, card_value):
        self.suit = suit
        self.card_name = card_name
        self.card_value = card_value

#class constructor for the deck
class deck:
    def __init__(self):
        self.current_deck = []
        self.suits = ['hearts', 'diamonds','spades','clubs']
        self.cards = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
    def initialize(self):
        for i in range(len(self.suits)):
            for j in range(len(self.cards)):
                if (self.cards[j]=='2' or self.cards[j]=='3' or self.cards[j]=='4' or self.cards[j]=='5' or self.cards[j]=='6' or self.cards[j]=='7' or self.cards[j]=='8' or self.cards[j]=='9'):
                    self.current_deck.append(card(self.suits[i], self.cards[j], int(self.cards[j])))
                elif (self.cards[j]=='10' or self.cards[j]=='jack' or self.cards[j]=='queen' or self.cards[j]=='king'):   
                    self.current_deck.append(card(self.suits[i], self.cards[j], 10))
                else:
                    self.current_deck.append(card(self.suits[i], self.cards[j], 11))
    def shuffle(self):
        for card in self.current_deck:
            j = random.randrange(0, len(playing_deck.current_deck))
            temp = card
            card = self.current_deck[j]
            self.current_deck[j] = temp

#class constrcutor for dealer
class dealer:
    def __init__(self):
        self.money = 10000
        self.hand = []
        self.hand_count = 0
    def hit(self, deck_):
        self.hand.append(deck_.pop())
    def deal(self, deck_, player_):
        for i in range (2):
            self.hand.append(deck_.current_deck.pop())
        for i in range (2):
            player_.hand.append(deck_.current_deck.pop())
    def strategy(self):
        print()
    def take_back_cards(self, deck_, player_):
        for i in range (2):
            self.hand.pop(deck_.append())
        for i in range (2):
            player_.hand.pop(deck_.append())        

#class constrcutor for players
class player: 
    def __init__(self, name):
        self.name = name
        self.money = 200
        self.hand = []
        self.hand_count = 0    
    def hit(self, deck_):
        self.hand.append(deck_.pop())


#create the player
print('Welcome to blackjack on the command line,\nYou have $200 to start with good luck!')
user = input('Please enter your name:\n')
Player = player(user)

#create the dealer
Dealer = dealer()

#create a deck that is shuffled
playing_deck = deck()
playing_deck.initialize()
playing_deck.shuffle()

while still_playing == True:
    


Dealer.deal(playing_deck, Player)

for i  in range(len(Player.hand)):
    print(vars(Player.hand[i]))

for i  in range(len(Dealer.hand)):
    print(vars(Dealer.hand[i]))

#Player.hit(playing_deck.current_deck)

#print(vars(Player))
#for i in range(len(playing_deck.current_deck)):
    #print(vars(playing_deck.current_deck[i]))


