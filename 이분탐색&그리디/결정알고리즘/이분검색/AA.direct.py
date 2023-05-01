import sys
sys.stdin = open('input.txt', 'rt')

N,M = map(int, input().split())

numberList = list(map(int, input().split()))

numberList.sort()
lt = 0
rt = len(numberList)-1

# lt가 rt와 같아지면 이분탐색이 종료되는 것임. 커질수는 없음.
# 탐색은 lt와 rt의 중간점의 값으로 이용.
# mid 값이 탐색하려는 값보다 크면, rt 조정 | 작으면 lt 조정
while lt <= rt:
    mid = (lt+rt)//2
    if numberList[mid] == M:
        print(mid+1)
        break
    elif numberList[mid] > M:
        rt = mid - 1
    else:
        lt = mid + 1


    
