import sys
sys.stdin = open('input.txt')

def check_card(cards):
    cards.sort()
    for i in range(len(cards)-2):
        for j in range(i+1, len(cards)-1):
            for k in range(j+1, len(cards)):
                if cards[i] == cards[j] and cards[i] == cards[k]:
                    return True
                if cards[i] + 1 == cards[j] and cards[j] + 1 == cards[k]:
                    return True
    return False

T = int(input())
for tc in range(T):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    count = 1
    winner = 0
    for card in cards:
        if count:
            p1.append(card)
            count = 0
            if len(p1) >= 3:
                if check_card(p1):
                    winner = 1
                    break
        else:
            p2.append(card)
            count = 1
            if len(p2) >= 3:
                if check_card(p2):
                    winner = 2
                    break
    print("#{} {}".format(tc+1, winner))