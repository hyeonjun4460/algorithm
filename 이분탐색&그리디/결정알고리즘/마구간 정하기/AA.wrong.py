import sys
from itertools import combinations
sys.stdin = open('input.txt', 'rt')

n,c = map(int, input().split())

# 말의 위치는 index+1 + value 값
# 말들을 위치시키기
# 가장 가까운 두 말의 거리(x)를 구하는 함수 구현
# x가 mid보다 크면 정답에 추가, lt = mid + 1
# x가 mid보다 작으면 정답에 추가, lt = mid + 1
# 거리 차의 합이 가장 큰 것 중, 가장 가까운 두 말의 거리가 최대인 것
# 
houses = list()


rt = 0
for i in range(n):
    x = int(input()) 
    houses.append(x)
    if rt <= x:
        rt = x
lt = 1
sample = list(combinations(houses,c))
print(sample)
while lt <= rt:
    mid = (lt+rt)//2
    
    


