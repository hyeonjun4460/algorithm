import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
a = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))

c = list()

r1=0
r2=0
# a,b 두 리스트의 값을 인덱스 하나씩 순차적으로 비교해서 새 리스트에 넣는다.
for i in range(N+M):
    if(r1 > N-1):
        c += b[r2:]
        break
    if(r2 > M-1):
        c += a[r1:]
        break
    if(a[r1] <= b[r2]):
        c.append(a[r1])
        r1+=1
    else:
        c.append(b[r2])
        r2+=1


for x in c:
    print(x, end=' ')