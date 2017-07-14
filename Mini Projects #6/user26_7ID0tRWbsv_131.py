# Mini-project #6 - Blackjack
# MY IMPLEMENTATION

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
#deck = []
in_play = False
outcome = ""
score = 0
game_deck = []
player_hands = []
dealer_hands = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.inventory = []
        
    def __str__(self):
        # return a string representation of a hand
        s = ""
        for t in self.inventory:
          s += str(t) + " "
        return "Hand contains: " + s

        
    def add_card(self, card):
        # add a card object to a hand
        self.inventory.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        total_value = 0
        val_list = []
        
        for x in self.inventory:
            val_list.append(VALUES[x.get_rank()])
            val_list.sort()
            val_list.reverse()
            
        for y in val_list:
            if (y == 1 and (total_value + 10 <= 21)):
                total_value += z * 10
            else:
                total_value += y
        print "Y=",val_list
        return total_value
           
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        offset = [0,0]
        for x in self.inventory:
            #x.card.draw(canvas, 400, 200)
            x.draw(canvas, [(pos[0] + offset[0]),(pos[1] + offset[1])])
            #print "Offset =", offset
            offset[0] += 75
            #offset[1] += 98
            #canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deckinventory = []
        # create a Deck object
        for s in SUITS:
            for r in RANKS:
                #card_var1 = Card(s,r)
                self.deckinventory.append(Card(s,r))
        #print "Self Inv= ", self.deckinventory

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deckinventory)

    def deal_card(self):
        # deal a card object from the deck
        return self.deckinventory.pop(0)  
    
    def __str__(self):
        # return a string representing the deck
        y = "Deck Inventory =" 
        for x in self.deckinventory:
            y += str(x) + " "
        #d = self.deckinventory
        #return str(d for d in self.deckinventory)
        return y

#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player_hands, dealer_hands

    # your code goes here
    game_deck = Deck()
    game_deck.shuffle()
    player_hands = Hand()
    dealer_hands = Hand()
    
    player_hands.add_card(game_deck.deal_card())
    player_hands.add_card(game_deck.deal_card())
    dealer_hands.add_card(game_deck.deal_card())
    dealer_hands.add_card(game_deck.deal_card())

    print "Player_hands=", player_hands
    print "Dealer_hands=", dealer_hands
    
    in_play = True

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global player_hands, dealer_hands
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BLACKJACK", [50,50],50,"Red")
    canvas.draw_text("Dealer", [40,160],30,"Cyan")
    canvas.draw_text("Player", [40,320],30,"Cyan")    
    card = Card("S", "A")
    dealer_hands.draw(canvas, [40, 180])
    player_hands.draw(canvas, [40, 360])
    #card.draw(canvas, [300, 300])
    #card.draw(canvas, [400, 200])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric