import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())

procession = list()
for _ in range(n):
    procession.append(list(map(int,input().split())))

print(procession)

# 전체합
answer = 0
for i in range(n):
    answer += sum(procession[i])

# 가장자리 없애기
for i in range(n//2):
    print(i, n//2 + 1 +i)
    answer = answer - procession[0][i] - procession[0][n//2 + 1 + i] - procession[-1][i] - procession[-1][n//2 + 1 + i] - procession[i][0] - procession[n//2 + 1 + i][0] - procession[i][-1] - procession[n//2 + 1 + i][-1]

answer += procession[0][0] + procession[0][-1] + procession[-1][0] + procession[-1][-1]
print(answer)