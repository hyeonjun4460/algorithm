import sys
sys.stdin = open('input.txt', 'rt')

N,M = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[lt]
cnt = 0

while True:
    if tot < M:
        if rt < N:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == M:
            cnt+=1
            tot -= a[lt]
            lt +=1
    elif tot > M:
            tot -= a[lt]
            lt += 1
    
print(cnt)
