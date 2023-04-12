import sys

# sys.stdin = open('input.txt', 'rt')

T = int(input())


for i in range(T):
    n,s,e,k = map(int,input().split())
    sample = list(map(int,input().split()))
    answer = sample[s-1:e]
    answer.sort()
    number = '#' + str(i+1)
    print(number, answer[k-1])