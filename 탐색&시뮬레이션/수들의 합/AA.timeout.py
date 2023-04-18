import sys
# sys.stdin = open('input.txt', 'rt')

N,M = map(int, input().split())

array = list(map(int, input().split()))

cnt = 0
for i in range(len(array)):
    for j in range(i,len(array)):
        if(sum(array[i:j+1]) == M):
            cnt+=1
            break
print(cnt)
