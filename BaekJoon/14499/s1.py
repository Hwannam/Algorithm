import sys
dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

def move(y,x, di):
    ny = y +

N,M,x,y,K = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().split()))