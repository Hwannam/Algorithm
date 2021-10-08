def plus_time(now_time):
    global finished
    while finished < n:
        for i in range(len(times)):
            if now_time % times[i] == 0:
                finished += 1
            if times[i] > now_time:
                now_time += 1
                break
    return now_time


def solution(n, times):
    finished = 0
    times.sort()
    now = 1
    answer = plus_time(now)
    return answer