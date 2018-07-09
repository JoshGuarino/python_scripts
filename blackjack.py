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
        self.hand_index = -1 
    def hit(self, deck_):
        self.hand_index += 1
        self.hand.append(deck_.current_deck.pop())
        current_card_name = self.hand[self.hand_index]
        self.hand_count += self.hand[self.hand_index].card_value    
        if self.hand_count > 21:
            for x in self.hand:
                if x.card_name == 'ace':
                    x.card_value = 1
                    self.hand_count -= 10
    def deal(self, deck_, player_):
        for i in range (2):
            self.hand_index += 1
            self.hand.append(deck_.current_deck.pop())
            current_card_name = self.hand[i]
            self.hand_count += self.hand[i].card_value
        for i in range (2):
            player_.hand_index += 1
            player_.hand.append(deck_.current_deck.pop())
            current_card_name = player_.hand[i]
            player_.hand_count += player_.hand[i].card_value    
    def strategy(self, deck_):
        while self.hand_count < 17:
            self.hit(deck_)
            if self.hand_count > 21:
                for x in self.hand:
                    if x.card_name == 'ace':
                        x.card_value = 1
                        self.hand_count -= 10
    def reset_table(self, deck_, player_):
        #reset dealer
        for x in range(self.hand_index + 1):
            if self.hand[x].card_name == 'ace':
                self.hand[x].card_value = 11
        for x in range(self.hand_index + 1):
            deck_.current_deck.append(self.hand.pop())
        self.hand_count = 0
        self.hand_index = -1

        #reset player
        for x in range(player_.hand_index + 1):
            if player_.hand[x].card_name == 'ace':
                player_.hand[x].card_value = 11
        for x in range(player_.hand_index + 1):
            deck_.current_deck.append(player_.hand.pop(0))        
        player_.hand_count = 0
        player_.hand_index = -1





#class constrcutor for players
class player: 
    def __init__(self, name):
        self.name = name
        self.money = 200
        self.hand = []
        self.hand_count = 0  
        self.hand_index = -1  
    def hit(self, deck_):
        self.hand_index += 1
        self.hand.append(deck_.current_deck.pop())
        current_card_name = self.hand[self.hand_index]
        self.hand_count += self.hand[self.hand_index].card_value
        if self.hand_count > 21:
            for x in self.hand:
                if x.card_name == 'ace':
                    x.card_value = 1
                    self.hand_count -= 10

#create the player
print('Welcome to blackjack on the command line,\nYou have $200 to start with good luck!')
user = input('Please enter your name:\n')
Player = player(user)
print('Welcome ' + Player.name + '! You have $200, good luck!')

#create the dealer
Dealer = dealer()

#create a deck
playing_deck = deck()
playing_deck.initialize()

#main game structure
while still_playing == True:

    #placing bet
    print('You have $' + str(Player.money) + ' currently.')
    bet_status = False
    while bet_status == False:
        try:
            bet = int(input('Please enter the amount of money you want to bet: \n'))
            while bet > Player.money:
                print('You have entered a bet that is greater than the amount of money you have.')
                bet = int(input('Please enter the amount of money you want to bet: \n'))
            Player.money -= bet
            Dealer.money += bet
            bet_status = True
        except ValueError:
            print('Error, you must enter a numerical money value.')
    
    #shuffle and deal cards
    playing_deck.shuffle()
    Dealer.deal(playing_deck, Player)   

    #player takes turn        
    hit_status = True
    while hit_status == True:
        print('Your hand is:')
        for i in range(len(Player.hand)):
            print(Player.hand[i].card_name + ' of ' + Player.hand[i].suit)
        print('Your hand count is now at ' + str(Player.hand_count) + '.')
        if Player.hand_count < 21:
            player_wants_hit = input('Would you like to hit? You can enter y/n for yes/no:\n')
            if (player_wants_hit.lower()=='y' or player_wants_hit.lower()=='yes'):
                Player.hit(playing_deck)
            elif (player_wants_hit.lower()=='n' or player_wants_hit.lower()=='no'):
                hit_status = False
            else:
                print('\nPlease enter a valid yes/no. You can use y/n.')
        elif Player.hand_count == 21:
            print("You have hit 21!!!\n")
            hit_status = False
        else:
            hit_status = False

    #dealer takes turn
    Dealer.strategy(playing_deck)
    print('Dealers hand is:')
    for i in range(len(Dealer.hand)):
        print(Dealer.hand[i].card_name + ' of ' + Dealer.hand[i].suit)
    print('Dealer hand count is at ' + str(Dealer.hand_count) + '.\n')

    #determine outcome
    if (Dealer.hand_count==Player.hand_count and Dealer.hand_count<22 and Player.hand_count<22):
        print('You have tied the dealer, you bet has been returned.')
        Player.money += bet
        Dealer.money -= bet
    elif (Dealer.hand_count>21 and Player.hand_count<21):
        print('The dealer has gone over, you win!')
        Player.money += bet*2
        Dealer.money -= bet*2
    elif (Dealer.hand_count<22 and Player.hand_count>21):
        print('You have gone over...')
    elif (Dealer.hand_count<22 and Player.hand_count<22 and Player.hand_count>Dealer.hand_count):
        print('You beat the dealer, you win!')
        Player.money += bet*2
        Dealer.money -= bet*2
    elif (Dealer.hand_count<22 and Player.hand_count<22 and Player.hand_count<Dealer.hand_count): 
        print('You have lost to the dealer...')
    
    #reset the table
    Dealer.reset_table(playing_deck, Player)

    #determine if player is still playing
    right_syntax = False
    while right_syntax == False:
        if Player.money == 0:
            still_playing = False
            right_syntax = True
            print('You have run out of money, better luck next time!')
        elif Dealer.money < 0:
            still_playing = False
            right_syntax = True
            print('Congrats you have broken the house!!!!!!!!')
        else:
            cont = input('Would you like to continue playing? You can enter y/n for yes/no:\n')
            if (cont.lower()=='y' or cont.lower()=='yes'):
                right_syntax = True
            elif (cont.lower()=='n' or cont.lower()=='no'):
                still_playing = False
                right_syntax = True
                print('Thanks for playing!')
            else:
                print('\nPlease enter a valid yes/no. You can use y/n.')

#for i  in range(len(Player.hand)):
    #print(vars(Player.hand[i]))
#print(str(Player.hand_count) + '\n' + str(Player.money) + '\n')

#for i  in range(len(Dealer.hand)):
    #print(vars(Dealer.hand[i]))
#print(str(Dealer.hand_count) + '\n' + str(Dealer.money))

#print(vars(Player))

#for i in range(len(playing_deck.current_deck)):
    #print(vars(playing_deck.current_deck[i]))