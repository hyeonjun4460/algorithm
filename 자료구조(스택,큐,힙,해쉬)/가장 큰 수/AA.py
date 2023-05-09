import sys
# sys.stdin = open('input.txt', 'rt')

n,m = input().split()

N = list(int(x) for x in n)
# cnt 가 m이 될 때까지
# 첫번쨰 값은 스택에 넣는다.
# 스택의 값보다 작으면 pass
# 스택의 값보다 크면 스택 값을 pop하고 새 값을 넣는다.
cnt = 0
stack = [str(N[0])]
index = 0
for i in range(1,len(n)):
    # 같거나 작으면 넣는다
    if int(stack[-1]) >= int(n[i]):
        stack.append(n[i])
    else:
        # 큰 값이 들어오면, 스택에 있는 값이 그 값과 같거나 클때까지 스택을 비운다
        while int(stack[-1]) < int(n[i]):
            stack.pop()
            cnt+=1
            if len(stack) == 0:
                break
            if cnt == int(m):
                index = i+1
                break
        stack.append(n[i])
    # m개 만큼 숫자를 뺐다면, 종료한다.
    if cnt == int(m):
        index = i+1
        break
# 반복을 다 순회했다면, 빼야되는 자리수만큼 stack을 비운다.
else:
    while cnt != int(m):
        stack.pop()
        cnt+=1

# 스택이 덜 채워졌다면, n의 남은 값들을 더해준다.
if len(stack) != len(n) - int(m):
    stack += n[index:]
for x in stack:
    print(x, end='')