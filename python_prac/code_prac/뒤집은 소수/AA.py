import sys
# sys.stdin = open('input.txt', 'rt')

N = int(input())

numbers = list(map(int, input().split()))

def reverse(x):
    numberList = list(str(x))
# 0뺴기
    for i in range(len(numberList)-1, -1, -1):
        if(numberList[i] == '0'):
            numberList.pop()
        else:
            break
    numberList.reverse()
    return int(''.join(numberList))
# 뒤집어서 합치기
# 0버리기


# 소수 판별하기

def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

answer = ''

for number in numbers:
    reverseNum = reverse(number)
    if (isPrime(reverseNum)):
        answer += str(reverseNum) + ' '
print(answer)
# 숫자 뒤집기
