import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())

procession = []
for _ in range(n):
    procession.append(list(map(int,input().split())))

s= n//2
e = n//2

answer = 0
for i in range(n):
    
    for j in range(s,e+1):
        print(i,j)
        answer += procession[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(answer)