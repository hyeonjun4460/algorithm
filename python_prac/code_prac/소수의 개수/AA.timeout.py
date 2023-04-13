import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

def isPrime(x):
    for i in range(2,x):
        if x%i ==0:
            return False
    return True

cnt=0
for n in range(2,N+1):
    if isPrime(n):
        cnt+=1

print(cnt)