import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split())
    l_A = l_B = 1
    r_A = r_B = P
    result_A = result_B = 0
    finish_A = finish_B = False

    while (finish_A == False) or (finish_B == False): # A와 B 모두 끝날때 까지
        if finish_A == False:          # A가 끝나지 않았을때 A 코드 동작
            c_A = int((l_A + r_A) / 2)
            result_A += 1 # 코드를 1회 돌리므로 1회 동작 추가
            if A == c_A:  # 수를 찾았을 때
                finish_A = True # A 코드는 더 안 돌리기 위함
            elif c_A < A:
                l_A = c_A
            else:
                r_A = c_A

        if finish_B == False: # B가 끝나지 않았을때 B 코드 동작
            c_B = int((l_B + r_B) / 2)
            result_B += 1 # 코드를 1회 돌리므로 1회 동작 추가
            if B == c_B: # 수를 찾았을 때
                finish_B = True # B 코드는 더 안 돌리기 위함
            elif c_B < B:
                l_B = c_B
            else:
                r_B = c_B

    if result_A > result_B:
        print("#{} B".format(tc + 1))
    elif result_B > result_A:
        print("#{} A".format(tc + 1))
    else:
        print("#{} 0".format(tc + 1))


