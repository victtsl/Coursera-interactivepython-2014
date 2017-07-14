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
in_play = False
#outcome = ""
score = 0
game_deck = []
player_hands = []
dealer_hands = []
player_busted_msg = ""
dealer_busted_msg = ""
is_player_busted = False
is_new_game = True

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
            if (y == 1 and (total_value + 11 <= 21)):
                total_value += y * 11
            else:
                total_value += y
        return total_value
           
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        offset = [0,0]
        for x in self.inventory:
            x.draw(canvas, [(pos[0] + offset[0]),(pos[1] + offset[1])])
            offset[0] += 75
        
        
# define deck class 
class Deck:
    def __init__(self):
        self.deckinventory = []
        # create a Deck object
        for s in SUITS:
            for r in RANKS:
                self.deckinventory.append(Card(s,r))

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
        return y

#define event handlers for buttons
def deal():
    global in_play, game_deck, player_hands, dealer_hands, player_busted_msg, dealer_busted_msg, is_player_busted, score, is_new_game

    # your code goes here
    game_deck = Deck()
    game_deck.shuffle()
    player_hands = Hand()
    dealer_hands = Hand()
    
    player_hands.add_card(game_deck.deal_card())
    player_hands.add_card(game_deck.deal_card())
    dealer_hands.add_card(game_deck.deal_card())
    dealer_hands.add_card(game_deck.deal_card())
    
    player_busted_msg = "Hit or stand?"
    dealer_busted_msg = ""
    is_player_busted = False
    
    #print "Player_hands=", player_hands
    #print "Dealer_hands=", dealer_hands
    #print "Dealer Val=", dealer_hands.get_value()
    #print "Player Val=", player_hands.get_value()

    
    if in_play and not is_new_game:
        dealer_busted_msg = "DEALER WINS! New deal?" 
        player_busted_msg = ""        
        score -= 1
        in_play = False 
    is_new_game = False
    in_play = True        
    #print "SCORE=", score    
    
def hit():
    global is_player_busted, in_play, score, player_busted_msg, dealer_busted_msg
    is_player_busted = False
    # if the hand is in play, hit the player
    if (player_hands.get_value() < 21 and in_play):
        player_hands.add_card(game_deck.deal_card())
    #print "Dealer Val=", dealer_hands.get_value()
    #print "Player Val=", player_hands.get_value()

    # if busted, assign a message to outcome, update in_play and score    
    if in_play and player_hands.get_value() > 21:
        is_player_busted = True
        player_busted_msg = "You have busted!"
        dealer_busted_msg = "DEALER WINS! New deal?"        
        score -= 1
        in_play = False        
    #print "SCORE1=", score    
    
       
def stand():
    global in_play, player_busted_msg, dealer_busted_msg, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    #in_play = False
    #print "Dealer Val=", dealer_hands.get_value()
    #print "Player Val=", player_hands.get_value()

    while (dealer_hands.get_value() < 17 and not is_player_busted):
        dealer_hands.add_card(game_deck.deal_card())

    if in_play and dealer_hands.get_value() > 21:
        dealer_busted_msg = "Dealer has busted!"
        player_busted_msg = "YOU WIN! New deal?"        
        score += 1
        in_play = False
    
    elif in_play and dealer_hands.get_value() < player_hands.get_value():
        player_busted_msg = "YOU WIN! New deal?"
        if in_play:
            score += 1
        in_play = False

    elif in_play and dealer_hands.get_value() >= player_hands.get_value():
        dealer_busted_msg = "DEALER WINS! New deal?"
        player_busted_msg = ""
        if in_play:
            score -= 1
        in_play = False
    #print "SCORE2=", score

# draw handler    
def draw(canvas):
    #global in_play, player_hands, dealer_hands, player_busted_msg, dealer_busted_msg, card_back, score

    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BLACKJACK", [50,50],50,"Red")
    canvas.draw_text("Dealer", [40,160],30,"Cyan")
    canvas.draw_text("Player", [40,340],30,"Cyan")    
    canvas.draw_text(player_busted_msg, [200,340],30,"Red")    
    canvas.draw_text(dealer_busted_msg, [200,120],30,"Red")        
    #canvas.draw_text(str(dealer_hands.get_value()), [150,160],30,"Cyan")
    #canvas.draw_text(str(player_hands.get_value()), [150,320],30,"Cyan")
    dealer_hands.draw(canvas, [40, 180])
    player_hands.draw(canvas, [40, 360])
    canvas.draw_text("Score", [340,160],30,"Black")
    canvas.draw_text(str(score), [450,160],30,"Black")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [76, 230], CARD_BACK_SIZE)

    
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