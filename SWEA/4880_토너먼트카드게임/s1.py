import sys
sys.stdin = open("input.txt")

def divide(i, j):
    if i == j:
        return i

    first = divide(i, (i + j) // 2)
    second = divide((i + j) // 2 + 1, j)
    return game(first, second)

def game(first, second):

    player1 = card[first]
    player2 = card[second]
    if abs(player1 - player2) == 2:
        if player1 > player2:
            return second
        else:
            return first
    elif abs(player1 - player2) == 1:
        if player1 < player2:
            return second
        else:
            return first
    else:
        return min(first, second)

T = int(input())
for tc in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    print("#{} {}".format(tc + 1, divide(0, N-1) + 1))