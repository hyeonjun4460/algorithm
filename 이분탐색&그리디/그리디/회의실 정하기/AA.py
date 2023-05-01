# 그리디
# 정렬 기준: 회의 끝나는 시간을 오름차순
# 이유
# 1. 회의가 끙나는 시간이 빠르다는건, 회의 시작 시간도 이르다는 것이다.
# 2. 회의가 끝나는 시간을 오름차순 정렬하면, 최대한 많은 회의를 비교하고, 실행할 수 있다.
import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())

meetings = list()

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key= lambda x: x[1])
# 그 다음 회의의 시작 시간이 이전 회의의 끝나는 시간보다 크거나 같으면 +, 끝나는 시간
#  바로미터 바꾸기
cnt = 1
end = meetings[0][1]
for i in range(1,len(meetings)):
    if meetings[i][0] >= end:
        cnt+=1
        end = meetings[i][1]
print(cnt)
