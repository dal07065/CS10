import random

deck = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

def create_deck()->dict:
    #dictionary = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3

    global deck
    cards = {}
    for deckType in deck:
        for i in range(1, 14):
            if i == 1:
                string = "Ace" + " of " + deckType
                cards[string] = i
            elif i == 11:
                string = "Jack" + " of " + deckType
                cards[string] = 10
            elif i == 12:
                string = "Queen" + " of " + deckType
                cards[string] = 10
            elif i == 13:
                string = "King" + " of " + deckType
                cards[string] = 10
            else:
                string = str(i) + " of " + deckType
                cards[string] = i
    for card in cards:
        print(card, ":", cards[card], sep='')
        if card.find("King") == 0:
            print()
            
    return cards

# **without using a dictionary**
##def deal_cards(numCards:int, cards:dict)->None:
##    global deck
##    for num in range(numCards):
##        deckType = random.randint(0,4)
##        cardValue = random.randint(1, 13)
##        if cardValue == 1:
##            string = "Ace" + " of " + deck[deckType]
##        elif cardValue == 11:
##            string = "Jack" + " of " + deck[deckType]
##        elif cardValue == 12:
##            string = "Queen" + " of " + deck[deckType]
##        elif cardValue == 13:
##            string = "King" + " of " + deck[deckType]
##        else:
##            string = str(cardValue) + " of " + deck[deckType]

## **using a dictionary**
def deal_cards(numCards:int, cards:dict)->None:
    global deck
    totalValue = 0
    for num in range(numCards):
        card = random.choice(list(cards.keys()))
        value = cards.pop(card)
        print(card)
        totalValue += value
    print("Total Value:", totalValue)

def main():
    cards = create_deck()

    rounds = int(input("How many rounds to deal cards? "))
    print()
    
    for num in range(rounds):
        howManyCards = int(input("How many cards should I deal? "))
        deal_cards(howManyCards, cards)
        print()
    
if __name__ == "__main__":
    main()
