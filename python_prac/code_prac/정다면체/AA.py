import sys
# sys.stdin = open('input.txt', 'rt')

N,M = map(int, input().split())

# N,M의 자리수
sumList = []
sumSet = set()
for n in range(1,N+1):
    for m in range(1,M+1):
        sumList.append(n+m)
        sumSet.add(n+m)

sumSet = list(sumSet)

sumSet = list(map(lambda x: {'value': x, 'count': sumList.count(x)}, sumSet))
sumSet.sort(key= lambda x: x['count'], reverse=True)

answer = ''
tmp = 0
for value in sumSet:
    if value['count'] >= tmp:
        tmp = value['count']
        answer += str(value['value']) + ' '
    else:
        break
print(answer)
# n,m을 더했을 때 나오는 경우의 수 총 개수
    