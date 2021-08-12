N = int(input())

number = list(map(int, input().split()))
plus_length = minus_length = max_length = 1
equal_length = 0

for i in range(len(number) - 1):
    if number[i] < number[i+1]:
        minus_length += equal_length # 감소하다가 증가한 경우, 이전까지 결과 처리
        if minus_length > max_length:
            max_length = minus_length
        minus_length = 1

        plus_length += 1 # 증가하는 경우이므로

        if equal_length != 0: # 2 2 2 3 이런식으로 증가하지만 같은게 있는 경우 반영
            plus_length += equal_length

        equal_length = 0 # equal에 대한 2가지 경우를 위에서 처리했으므로

    elif number[i] > number[i+1]:
        plus_length += equal_length # 증가하다가 감소한 경우, 이전까지 결과 처리
        if plus_length > max_length:
            max_length = plus_length
        plus_length = 1

        minus_length += 1 # 감소하는 경우이므로

        if equal_length != 0: # 2 2 2 1 이런식으로 감소하지만 같은게 있는 경우 반영
            minus_length += equal_length

        equal_length = 0 # equal에 대한 2가지 경우를 위에서 처리했으므로

    else: # 증가 감소 하지 않으면 같은 수가 반복되는 것이므로 equal 증가
        equal_length += 1

if equal_length != 0: # 3 2 2 2 처럼 마지막에 equal이라 최종 결과가 반영되지 않는 경우를 해결
    if plus_length != 1:
        plus_length += equal_length
    elif minus_length != 1:
        minus_length += equal_length

# 최종 처리된 결과들을 비교해서 max 도출
# 5 5 5 5 5 처럼 equal만 나오는 경우가 있으므로 equal_length에 1을 더해서 비교(초기값이 0이므로)
max_length = max(plus_length, minus_length, equal_length + 1, max_length)
print(max_length)
