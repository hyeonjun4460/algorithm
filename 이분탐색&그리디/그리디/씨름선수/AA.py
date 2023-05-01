import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())

players = list()
for _ in range(n):
    players.append(list(map(int,input().split())))


players.sort(key= lambda x: (x[0],x[1]), reverse=True)

# 둘 다 작으면 빼기
# 하나라도 더 크면 살리기
# 키 기준점
# 몸무게 기준점
# 통과된 기준점은 그 다음사람 키나 몸무게로 대체
hp = players[0][0]
wp = players[0][1]
cnt = len(players)
for i in range(1,len(players)):
    h,w = players[i][0], players[i][1]
    stack = 0
    if h >= hp:
        hp = h
        stack +=1
    if w >= wp:
        wp = w
        stack +=1
    if stack <1:
        cnt -=1
print(cnt)
    