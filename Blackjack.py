import random
import time

deck = []
types = ("H", "C", "S", "D")
values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
player = []
dealer = []


def shuffleDeck():
    player.clear()
    dealer.clear()
    for cardtype in types:
        for value in values:
            deck.append(cardtype + "-" + value)

    random.shuffle(deck)


def hit(turn):
    turn.append(deck.pop(0))


def aceCheck(drawnCards):
    i = 0
    for card in drawnCards:
        if card[-1] == "A":
            i += 1
    return i


def getValue(drawnCards):
    x = []
    y = []
    z = 0
    for i in range(0, len(drawnCards)):
        x.append((drawnCards[i][-1]))
    for item in x:
        if item == "J" or item == "Q" or item == "K" or item == "0":
            item = item.replace(item, "10")
        if item == "A":
            item = item.replace(item, "11")
        y.append(item)
    for value in y:
        z += int(value)
    return z


def finalSum(drawnCards):
    sum = getValue(drawnCards)
    numberOfAces = aceCheck(drawnCards)
    while sum > 21 and numberOfAces != 0:
        if numberOfAces != 0:
            sum = sum - 10
            numberOfAces = numberOfAces - 1
    return sum


def playerLogic():
    print("your cards", player)
    print(finalSum(player))
    playerinput = input("Its your turn, Would you like to hit or stand")
    if playerinput == "hit":
        hit(player)
        if finalSum(player) > 21:
            print("your cards", player)
            print(finalSum(player))
            print("you went over 21")
            return
        playerLogic()
    elif playerinput == "stand":
        print("dealers turn")


def dealerLogic():
    while finalSum(dealer) < 17:
        hit(dealer)
        print("dealers cards", dealer)
        time.sleep(1)


def gameLogic():
    if finalSum(player) > 21:
        print("dealer won")
    elif finalSum(dealer) > 21:
        print("you won")
    elif finalSum(player) > finalSum(dealer):
        print("you won")
    elif finalSum(player) == finalSum(dealer):
        print("draw")
    else:
        print("dealer won")


def gameSession():
    shuffleDeck()
    hit(dealer)
    print("dealers cards", dealer)
    print(finalSum(dealer))
    hit(player)
    hit(player)
    playerLogic()
    dealerLogic()
    print(finalSum(dealer))
    gameLogic()
    if input("Another round?") == "yes":
        gameSession()
    else:
        return


gameSession()
