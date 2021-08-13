number = int(input())
dice = []
for _ in range(number):
    temp = list(map(int, input().split()))
    temp[1], temp[5] = temp[5], temp[1]
    temp[2], temp[5] = temp[5], temp[2]
    temp[4], temp[5] = temp[5], temp[4]
    dice.append(temp)

def find_pair(idx):
    if idx % 2 == 0:
        return idx + 1
    else:
        return idx - 1

def find_max(dice, up, pair):
    if dice[up] == 6 or dice[pair] == 6:
        if dice[up] == 5 or dice[pair] == 5:
            return 4
        else:
            return 5
    else:
        return 6

result = 0
for upside_idx in range(6):
    upside = dice[0][upside_idx]
    pair = find_pair(upside_idx)
    max_side = find_max(dice[0], upside_idx, pair)
    for j in range(1, number):
        pair = dice[j].index(upside)
        upside_idx = find_pair(pair)
        upside = dice[j][upside_idx]
        max_side += find_max(dice[j], upside_idx, pair)
    result = max(result, max_side)
print(result)