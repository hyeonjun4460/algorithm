import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

# 행/열 모두 인덱스 1부터 n-1까지

# stage = list(map(int, input().split()))

# stage.insert(0, [0]*N)
# stage.append([0]*N)

# for x in stage:
#     stage.insert(0,0)
#     stage.append(0)
# 상하좌우보다 값이 크면 cnt ++, 아니면  continue
stage = list([0]*(N+2) for _ in range(N+2))

for i in range(1, len(stage)-1):
    stage[i][1:len(stage)-1] = map(int,input().split())

answer = 0
for i in range(1,len(stage)-1):
    for j in range(1,len(stage)-1):
        target = stage[i][j]
        left = stage[i][j-1]
        right = stage[i][j+1]
        up = stage[i-1][j]
        down = stage[i+1][j]
        if target > left and target > right and target > up and target > down:
            answer +=1
        else:
            continue
print(answer)

