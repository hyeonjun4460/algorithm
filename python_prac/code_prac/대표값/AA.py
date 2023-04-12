import sys
# sys.stdin = open('input.txt', 'rt')

number = int(input())
students = list(map(int,input().split()))

# 평균 구하기
average = round(sum(students)/len(students))

# 평균과 가까운 학생 구하기
sample = list(map(lambda x: x-average, students))

statue = []
for i in range(len(students)):
    statue.append((i, students[i]-average))

statue.sort(key=lambda x: abs(x[1]))
# 높은 점수 학생 구하기
for i in range(len(statue)):
    first = statue[i]
    second = statue[i+1]
    firstPoint = first[1] + average
    secondPoint = second[1] + average
    if(first[1] == second[1]):
        if(first[0] < second[0]):
            print(average, first[0]+1)
            break
        else:
            print(average, second[0]+1)
            break
    if(abs(first[1]) == abs(second[1])):
        if (firstPoint >= secondPoint):
            print(average, first[0]+1)
            break
        if(firstPoint < secondPoint):
            continue
    print(average, first[0]+1)
    break
# 높은 점수 학생이 여러명이면 index 값이 빠른 게 정답
