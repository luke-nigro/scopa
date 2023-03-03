'''TODO:
    1. define the start game method (deal 3 cards to each player and play 4 to the table)
    2. define the play turn method (will define how cards can be captured)
'''
import random

class Card:

    def __init__(self, suit=None, value=None):
        
        self.suit=suit
        self.value=value

    def __str__(self):
        return '{value} of {suit}'.format(value=self.value, suit=self.suit)


class Deck:

    def __init__(self):
        self.cards = []
        self.suits = ['Denari', 'Coppe', 'Spade', 'Bastoni']
        self.build()

    def build(self):
        for suit in self.suits:
            for value in range(1,11):
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def is_empty(self):
        return len(self.cards) == 0
    
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.capture_pile = []

    def __str__(self):
        return '{name} currently has {points} points'.format(name=self.name, points=self.score)
    
    def play_card(self, game):
         # Allow the player to select a card from their hand and play it on the table
        card_index = None
        while card_index is None:
            print(f"{self.name}'s hand:")
            for i, card in enumerate(self.hand):
                print(f"{i}: {card}")
            try:
                card_index = int(input("Enter the index of the card you want to play: "))
                played_card = self.hand.pop(card_index)
                game.update_table(played_card)

                if len(game.table) == 0:
                    self.score += 1
                    print('scopa!')

            except (ValueError, IndexError):
                print("Invalid input, please try again.")
                card_index = None

    def capture_card(self,cards):
        self.capture_pile.extend(cards)

class Game:

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.deck.shuffle()
        self.table = []
        self.current_player_index = 0
        self.game_over = False

    def start(self):
        pass

    def play_turn(self):
        pass

    def update_table(self, played_card):
        
        self.table.append(played_card)

    def end_round(self):
        for player in self.players:
            # TODO redefine sum to fit the scopa criteria
            player.score += sum(1)
            player.captured_pile = []

    def capture_cards(self, cards):
        # Add captured cards to the current player's captured pile
        current_player = self.players[self.current_player_index]
        current_player.capture_cards(cards)

    def check_winner(self):
        # Check if any player has won the game
        for player in self.players:
            if player.score >= 11:
                if all(player.score - other_player.score >= 2 for other_player in self.players if other_player != player):
                    self.game_over = True
                    return player

        return None