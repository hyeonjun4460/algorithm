import sys
# sys.stdin = open('input.txt', 'rt')

N = int(input())

# 격자판 만들기
stage = list()

for _ in range(N):
    stage.append(list(map(int,input().split())))

downRight =0
upRight = 0
# 각 대각선의 합
for i in range(len(stage)):
    downRight += stage[i][i]
    upRight += stage[i][-1-i]
tot = 0

if downRight <= upRight:
    tot = upRight
else:
    tot = downRight

# 각 행의 합
for i in range(len(stage)):
    row = sum(stage[i])
    column = 0
    if (tot <= row):
        tot = row
    for j in range(len(stage)):
        column += stage[j][i]
    if(tot <= column):
        tot = column

print(tot)
# row, column 파라미터 이용하기


