import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())

numbers = list(map(int, input().split()))


# 최대값은 언제나 마지막 열에 있음
answer = list(float('inf') for _ in range(n))

# cnt를 충족하면 break하기
for i in range(n):
    cnt = 0
    index = 0
    for j in range(len(answer)):
        if answer[j] > i+1:
            cnt+=1
        if cnt == numbers[i]:
            index = j+1
            break
    if answer[index] != float('inf'):
            # 만약 넣어야 할 곳에 이미 값이 있다면, 그 뒤 index 중 inf를 가진 가장 가까운 곳에 값을 넣기
            infIndexs = list(filter(lambda x: answer[x] == float('inf'), range(index+1, len(answer))))
            answer[infIndexs[0]] = i +1
    else:
        answer[index] = i + 1
print(' '.join(str(x) for x in answer))
    