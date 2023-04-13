import sys
# sys.stdin = open('input.txt', 'rt')

N = int(input())

numbers = list(map(int, input().split()))

def digit_sum(x):
    statue = list(map(int,str(x)))
    return sum(statue)

tmp= 0
answer = 0
for number in numbers:
    digitSum = digit_sum(number)
    if (digitSum > tmp):
        tmp = digitSum
        answer = number
    elif (digitSum == tmp):
        continue
        
print(answer)

