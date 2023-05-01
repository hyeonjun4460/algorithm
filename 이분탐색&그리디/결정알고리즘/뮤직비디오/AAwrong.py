import sys
sys.stdin = open('input.txt', 'rt')

n,m = map(int, input().split())

# 시작점은 list의 sum
# list 안의 값을 순차적으로 더한 tmp값이 시작점의 값이 되면, cnt += 1, tmp =0하기
# cnt가 m과 동일하면 return, 아니면 시작점 바꾸기

songs = list(map(int, input().split()))

lt = 1
rt = sum(songs)
def check(mid):
    tmp = 0
    cnt = 0
    print('start',mid)
    res = []
    for i in songs:
        tmp += i
        print(i,tmp)
        if tmp >= mid:
            cnt += 1
            res.append(tmp)
            tmp = 0
    if cnt == m:
        res.sort()
        return res[-1]
    elif cnt > m:
        return 1
    else:
        return 2

    

while lt <= rt:
    mid = (lt + rt)//2
    statue = check(mid)
    if statue == 1:
        lt = mid+1
    elif statue == 2:
        rt = mid -1
    else:
        print(statue)
        break