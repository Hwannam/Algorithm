import sys
sys.stdin = open('input.txt')

def card_change(card, time, count):
    global max_money
    global found
    count += 1
    for i in range(0, len(card)-1):
        for j in range(i+1, len(card)):
            if found:
                return
            card[i], card[j] = card[j], card[i]
            if card == max_money_list: # 최대값과 같으면
                if (time - count)%2 == 0:
                    max_money = int("".join(map(str,card)))
                else:
                    card[-1], card[-2] = card[-2], card[-1]
                    max_money = int("".join(map(str, card)))
                found = True
                return
            elif count == time:
                max_money = max(max_money, int("".join(map(str, card))))
            else:
                card_change(card, time, count)
            card[i], card[j] = card[j], card[i]
    return

T = int(input())
for tc in range(T):
    info, max_time = map(int, input().split())
    card = []
    info = str(info)
    for char in info:
        card.append(int(char))
    max_money_list = sorted(card, reverse=True) # 최대 값 찾기
    max_money = 0
    found = False

    card_change(card, max_time, 0)
    print("#{} {}".format(tc+1, max_money))