import sys
# sys.stdin = open('input.txt', 'rt')

N,M = map(int, input().split())

numberList = list(map(int, input().split()))

numberList.sort()

print(numberList.index(M) + 1)