import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    num = int(input())
    prime = {2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0} # 2 3 5 7 11에 대한 dictionary

    for key in prime.keys(): # 2 3 5 7 9에 대하여
        while True:
            if num % key != 0: # 더 이상 분해가 되지 않으면 다음 소인수로
                break
            num /= key  # 분해가 된다면 num을 소인수로 나눈 값으로 업데이트
            prime[key] += 1 # 분해한 소인수의 개수를 증가

    print("#{}".format(tc+1), end = " ")
    count = 0
    for value in prime.values(): # dictionary의 각 소인수 key 에 대한 value 출력
        print(value, end = " ")
    print()