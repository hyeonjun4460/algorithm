# 결정 알고리즘의 특징: 정답의 범위가 뚜렷하게 보인다.
# 조건을 충족한 이후에는 가장 만족스러운 값을 찾도록 구현하는 것이 결정알고리즘이다.
import sys
# sys.stdin = open('input.txt', 'rt')

k,n = map(int, input().split())

lanList = list(int(input()) for _ in range(k))

lanList.sort()

length = lanList[-1]
lt = 1
rt = length
res = 0
# 아래 이분탐색은 while문이 끝까지 순회하기는 한다.
while lt <= rt:
    mid = (lt+rt)//2
    # 미드 값으로 나눈 몫의 합 구하기
    a = sum(list(map(lambda x: x//mid, lanList)))
    # 조건이 충족됐다면, 더 나은 최대값 찾기
    if a >= n:
        res = mid
        lt = mid+1
    # 조건이 충족되지 않으면 rt 값을 줄여서 탐색 범위 조정
    else:
        rt = mid-1

print(res)

    
