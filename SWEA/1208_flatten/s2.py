import sys
sys.stdin = open("input.txt")

# 내장함수 사용 X
for tc in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    max = min = box[0]               # max와 min의 값을 0번 index 값으로 초기 설정
    max_index = min_index = 0        # max와 min값을 갖는 index를 0으로 초기 설정

    for _ in range(dump):           # dump 만큼 반복
        for i in range(len(box)):   # box안의 max와 min 값과 각각의 index를 찾는 반복문
            current = box[i]
            if max < current:
                max = current
                max_index = i
            elif min > current:
                min = current
                min_index = i
        if (max - min) > 1:         # 평탄화 작업 미완료시
            box[max_index] -= 1     # 찾은 max와 min값을 가지는 index에서 1만큼 이동 시킴
            max -= 1
            box[min_index] += 1
            min += 1
        else:                       # dump 횟수 모두 소진 전에 평탄화 작업 완료시 종료 (문제 조건에 따라)
            break

    for i in range(len(box)):       # 작업 모두 종료후 max와 min이 달라졌을 수 있으므로 마지막으로 max, min 찾기
        current = box[i]
        if max < current:
            max = current
        elif min > current:
            min = current
    print("#{} {}".format(tc + 1, max - min))