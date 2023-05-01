import sys
sys.stdin = open('input.txt', 'rt')

n,m = map(int, input().split())
# 오답이유
# 1: dvd 용량은 언제나 songs 리스트의 최대값보다 커야하는 것이 간과됨
# 2: dvd에 songs를 삽입하는 조건문의 순서가 잘못됨.
# - songs를 삽입했을 떄, dvd에 쌓인 값이 dvd 용량을 초과하면, dvd 개수 추가 + 새 dvd에 song 삽입하는 로직이어야 함.
# - 기존 로직은 삽입 후, dvd에 쌓인 값이 용량을 초과했을 떄, dvd에 song을 삽입하지 않음
# - dvd 개수는 m보다 작아도 통과되어야 하지만 그렇지 않았음.

songs = list(map(int, input().split()))

lt = 1
rt = sum(songs)
def check(mid):
    tmp = 0
    cnt = 1
    for i in songs:
        if tmp + i > mid:
            cnt += 1
            tmp = i
        else:
            tmp += i
    return cnt

    
res = 0
while lt <= rt:
    mid = (lt + rt)//2
    statue = check(mid)
    if mid >= max(songs) and check(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)