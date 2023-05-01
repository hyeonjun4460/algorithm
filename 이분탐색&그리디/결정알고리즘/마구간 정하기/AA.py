# 풀이가 어려웠던  이유
# C마리의 말을 N개의 마구간에 넣는다고 했을 때, 그 조합의 경우의 수를 먼저 생각함.
# 문제에서 초점을 두어야 할 점은 "가장 가까운 말의 최대거리"임.
# 가장 가까운 말의 최대거리라는 말은, 남은 말들 간의 거리는 그 거리 이상임.
# 그러므로, 거리에 초점을 두고, 말둘 간의 거리가 가장 가까운 말의 최대거리(mid)보다 긴 개수가 c개 이상인지만 보면됨.
import sys
from itertools import combinations
sys.stdin = open('input.txt', 'rt')

n,c = map(int, input().split())
houses = list()



for _ in range(n):
    houses.append(int(input()))
lt = 1
houses.sort()
rt = houses[-1]
res = 0

def solution(mid):
    cnt = 1
    tmp = houses[0]
    for i in range(1, len(houses)):
        if (houses[i] - tmp) >= mid:
            cnt+=1
            tmp = houses[i]
    return cnt

while lt <= rt:
    mid = (lt + rt)//2
    if solution(mid) >= c:
        res = mid
        lt = mid +1
    else:
        rt = mid -1
print(res)