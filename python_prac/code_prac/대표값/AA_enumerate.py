import sys
sys.stdin = open('input.txt', 'rt')

number = int(input())
students = list(map(int,input().split()))

# 평균 구하기
average = round(sum(students)/len(students))

min = float('inf')
# 배열 안의 값을 (index, value)로 묶어서 볼 때 유용
# 최소값 구하는 기본 알고리즘을 이용해서 조건에 충족하는 데이터를 변경 및 유지
for index, x in enumerate(students):
    tmp = abs(x- average)
    print(index,x,tmp)
    if (tmp < min):
        min = tmp
        score = x
        res = index +1
    if (tmp == min):
        if score < x:
            res = index +1
            

print(average, res)