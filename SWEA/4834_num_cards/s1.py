import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    cards = int(input())
    list_card = []
    list_card.extend(input())
    result = [list_card[0], list_card.count(list_card[0])]

    for card in list_card:
        if list_card.count(card) > result[1]:
            result[0] = card
            result[1] = list_card.count(card)
        elif list_card.count(card) == result[1]:
            if result[0] < card:
                result[0] = card

    print("#{} {} {}".format(tc + 1, result[0], result[1]))