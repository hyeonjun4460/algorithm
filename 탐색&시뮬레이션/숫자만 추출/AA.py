import sys
sys.stdin = open('input.txt', 'rt')

data = list(input())

number = ''
# 숫자만 빼기
# isdigit(), isdeciaml() 활용하면 예외처리 안써도 됨
for i in range(len(data)):
    try:
        int(data[i])
        number += data[i]
    except ValueError:
        continue

answer = number
# 앞의 0 제거하기
for x in number:
    if x == '0':
        answer = answer.replace(x,'',1)
    else:
        break
# 약수 개수 구하기
cnt = 0
for i in range(1,int(answer)+1):
    if int(answer) % i == 0:
        cnt+=1
# 정답
print(answer)
print(cnt)

# 
    