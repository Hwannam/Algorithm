import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    result = 0

    weight.sort(reverse=True) # 내림차순 정렬
    truck.sort(reverse=True)
    for i in range(M):
        for j in range(len(weight)): # 가장 큰 트럭이 큰 컨테이너를 옮긴다.
            if truck[i] >= weight[j]:
                result += weight[j]
                weight.pop(j)
                break
    print("#{} {}".format(tc+1, result))
