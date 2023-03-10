import random 

suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card():
  """Class to make and return cards"""
  def __init__(self, new_rank, new_suit):
    self.rank = new_rank
    self.suit = new_suit

  def __repr__(self):
    return self.rank + " of " + self.suit
  
deck = []
for suit in suit:
  for rank in RANKS:
    deck.append(Card(rank, suit))
random.shuffle(deck)
p1  = deck[:5]
rank_list = {}

for ranks in RANKS:
    rank_list[ranks]=0
    
for card in p1:
    rank_list[card.rank] += 1
rank_list = list(rank_list.values())

flush = True

for card in p1:
    if p1[0].suit == card.suit:
        flush = False

if rank_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1] and flush:
    print("royal flush")
if str(rank_list).count("11111") and flush == True:
    print("straight flush")
elif rank_list.count(1) == 4:
    print("four of a kind")
elif rank_list.count(3) == 1 and rank_list.count(2) == 1:
    print("full house")
elif flush:
    print("flush")
elif str(rank_list).count("11111") == 1:
    print("straight")
elif rank_list.count(3) == 1:
  print("Three of a kind!!!")
elif rank_list.count(2) == 2:
    print("two pair")
if rank_list.count(2) == 1:
  print("one pair!!!")
else:
  print("Garbage")

