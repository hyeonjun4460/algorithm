import sys
# sys.stdin = open('input.txt', 'rt')

N = int(input())

# 상금 계산하기
def defineReward(x):
    x_set = list(set(x))
    if (len(x) == len(x_set)):
        return max(x)*100
    else:
        for n in x_set:
            if(x.count(n) == 3):
                return 10000 + (n*1000)
            if(x.count(n)==2):
                return 1000 + (n*100)


answer = 0
for i in range(N):
    numbers = list(map(int, input().split()))
    reward = defineReward(numbers)
    if reward > answer:
        answer = reward
print(answer)


# 가장 큰 상금만 남기기