import random

cards = []
suits = ["clubs", "hearts", "spades", "diamonds"]
ranks = []

specials = {"A": 11, "J": 10, "Q": 10, "K": 10}

for r in ["A"] + [str(i) for i in range(2, 11)] +["J", "Q", "K"]:
    if r in specials:
        value = specials[r]
    else:
        value = int(r)
    ranks.append({"rank": r,
                  "value": value})

print(ranks)

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()

