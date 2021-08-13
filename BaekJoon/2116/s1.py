number = int(input())
pairs = [0, 5, 1, 3, 2, 4] # 마주 보는 면끼리 붙어있다.
dice = []

for _ in range(number):
    dice.append(list(map(int, input().split())))

result = 0
for upside in dice[0]:
    max_side = 0
    upside_index = -1
    idx = dice[0].index(upside)  # 이전의 윗면의 현재 index
    pair = pairs.index(idx)  # idx가 마주보는 면의 index 찾기
    if pair % 2 == 0:
        upside_index = pairs[pair + 1]
    else:
        upside_index = pairs[pair - 1]
    if dice[0][idx] == 6 or dice[0][upside_index] == 6:
        if dice[0][idx] == 5 or dice[0][upside_index] == 5:
            max_side += 4
        else:
            max_side += 5
    else:
        max_side += 6

    for i in range(1, number): # 2번째 주사위부터
        idx = dice[i].index(upside) #이전의 윗면의 현재 index
        pair = pairs.index(idx) # idx가 마주보는 면의 index 찾기 과정
        if pair % 2 == 0:
            upside_index = pairs[pair + 1]
        else:
            upside_index = pairs[pair - 1]
        upside = dice[i][upside_index]
        if dice[i][idx] == 6 or dice[i][upside_index] == 6:
            if dice[i][idx] == 5 or dice[i][upside_index] == 5:
                max_side += 4
            else:
                max_side += 5
        else:
            max_side += 6
    result = max(result, max_side)

print(result)