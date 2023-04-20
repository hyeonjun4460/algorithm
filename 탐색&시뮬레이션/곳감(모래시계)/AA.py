import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')

N = int(input())
stage = list()
for _ in range(N):
    stage.append(list(map(int, input().split())))

M = int(input())
for _ in range(M):
    s,e,w = map(int,input().split())
    # 회전시키기
    if e == 0:
        w = -w
    option = deque(stage[s-1])
    option.rotate(w)
    stage[s-1] = list(option)

# 모리시계 값 구하기

a = 0
b = N-1
cnt = 0
for i in range(N-1):
    for j in range(a,b+1):
        cnt += stage[i][j]
    
    if i < j:
        a += 1
        b -= 1
    # i가 j보다 큰 경우에는 다시 늘어나야 하므로.
    # 다이아몬드는 a,b를 같은 값으로 두므로 조건분기를 a의 크기로 하면 됐다.
    # 모래시계는 a,b가 극점에서 좁아졌다가 다시 멀어져야하는 구조이고, a는 b보다 반드시 작아야한다.
    # 이에, i와 j를 분기로 삼았다.
    else:
        a -= 1
        b += 1

cnt += sum(stage[-1])
print(cnt)