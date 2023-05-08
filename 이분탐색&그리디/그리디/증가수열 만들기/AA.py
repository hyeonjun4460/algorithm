# 첫 시작은 무조건 왼쪽과 오른쪽 중 더 작은 값으로 시작
# 둘 모두가 중간값을 넘기면 pass

import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())

numbers = list(map(int, input().split()))

last = 0
lt = 0
rt = n-1
words = ''
cnt = 0
tmp = []
while lt < rt:
    if last < numbers[lt]:
        tmp.append([numbers[lt],'L'])
    if last < numbers[rt]:
        tmp.append([numbers[rt],'R'])
    tmp.sort(key=lambda x: x[0])
    if len(tmp) == 0:
        break
    if last < tmp[0][0]:
        words += tmp[0][1]
        last = tmp[0][0]
        cnt+=1
    if tmp[0][1] == 'L':
        lt += 1
    else:
        rt -= 1
    tmp.clear()
print(cnt)
print(words)

        
    






