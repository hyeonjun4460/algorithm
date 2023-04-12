# 복수의 값을 리턴할 경우, 튜플 형태로 값이 반환됨
def sum(a,b):
    return a+b , a-b
print(sum(1,2))


a = [12,13,7,9,13]

# 소수 판별 함수
def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

for i in a:
    if isPrime(i):
        print(i, end=' ')