import sys
from itertools import combinations
sys.stdin = open('input.txt', 'rt')

n,c = map(int, input().split())
houses = list()


for i in range(n):
    houses.append(int(input()))
rt = 0
lt = 1
print(houses)
def solution(houses, c):
    sample = list(combinations(houses, c))
    print(sample)
    for i in range(len(sample)):
        for j in range(len(sample[i])):
            tmp = float('inf')
            for k in range(j+1, len(sample[i])):
                a = abs(sample[i][j] - sample[i][k])
                if tmp > a:
                    tmp = a
            if tmp > a:
                tmp = a
        print(tmp)

solution(houses,c )
