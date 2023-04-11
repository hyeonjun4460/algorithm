# range(n): 0부터 n-1까지 연속된 정수를 생성
# 역순을 구현하고 싶으면 -1을 주입해야함.
a = range(5)
b = range(1,11)
c = range(10,0,-1)
print(list(c))
# range를 이용한 for문
for i in range(10):
    print(i, 'hello')


# while
i = 1
while i <= 10:
    print(i)
    i+=1

i = 0
# break, continue
while True:
    if i == 6:
        print(i)
        break
    if i % 1 != 0:
        print('continue')
        continue
    i += 2


#  for, else : for문이 정상종료할 때에만 else 출력
for i in range(5):
    print(i)
    if i > 15:
        break
else:
    print(11)


# prac1: 1부터 n까지 홀수 출력

a = int(input())

for i in range(1,a+1):
    if (i%2 ==1):
        print(i)

# prac2: 1부터 n까지의 합

sumnumber = 0
for i in range(1,a+1):
    sumnumber+= i
print(sumnumber)

# prac3: N의 약수 출력
for i in range(1,a+1):
    if(a%i ==0):
        print(i)


# 중첩 반복문
# 1. n,m 길이의 사각형 만들기

n,m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print('*', end=' ')
    print() # 줄바꿈, 없으면 *만 계속 출력함.

# 2. 피라미드

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

# 3. 역피라미드

for i in range(n):
    for j in range(n-i):
        print('*', end=' ')
    print()
