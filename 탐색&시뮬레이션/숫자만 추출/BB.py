import sys
sys.stdin = open('input.txt', 'rt')

data = list(input())

# 숫자만들기
# isdigit(), isdeciaml() 활용하면 예외처리 안써도 됨
number = 0
for i in range(len(data)):
    if(data[i].isdecimal()):
        number = number*10 + int(data[i])

cnt = 0
for i in range(1,number+1):
    if number % i == 0:
        cnt+=1
# 정답
print(number)
print(cnt)

# 
    