import sys
# sys.stdin = open('input.txt', 'rt')

n,m = map(int, input().split())

weights = list(map(int, input().split()))


weights.sort()

# 양 끝을 더해서 m과 비교
# 작거나 같으면 탑승
# 크면 맨 끝을 pop하기
cnt = 0
outs = list()
while len(weights) != 0:
    if len(weights) == 1:
        cnt+=1
        outs.append(weights.pop())
    else:
        if weights[0] + weights[-1] <= m:
            cnt +=1
            weights.remove(weights[0])
            weights.remove(weights[-1])
        else:
            cnt+=1
            outs.append(weights.pop())
print(cnt)