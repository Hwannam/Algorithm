import sys
sys.stdin = open("input.txt")

# 내장함수 sort 사용
for tc in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        box.sort()                  # Sort를 통해서 앞쪽에 가장 낮은, 뒤쪽에 가장 높은 상자를 배치
        if (box[99] - box[0]) > 1:  # 가장 낮은 것과 가장 높은 것의 차이가 1이하일 경우 평탄화 완료
            box[99] -= 1            # 가장 높은 상자를 하나 빼서 가장 낮은 곳에 옮긴다.
            box[0] += 1
        else:                       # 문제의 조건에 따라 평탄화 작업 완료시 더 진행할 필요가 없다!
            break

    box.sort()                      # dump후 마지막 정렬
    print("#{} {}".format(tc + 1, box[99] - box[0]))