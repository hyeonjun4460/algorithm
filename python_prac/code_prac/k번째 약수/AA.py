import sys
# sys.stdin = open('input.txt', 'rt')

n,k = list(map(int, input().split()))

def solution(n,k):
    cnt = 0
    for i in range(1,n+1):
        if n%i ==0:
            cnt +=1
        if cnt == k:
            return i
    else:
        return -1
    
print(solution(n,k))
        