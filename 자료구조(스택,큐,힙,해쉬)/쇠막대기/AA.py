import sys
sys.stdin = open('input.txt', 'rt')

line = list(input())

print(line)

a = [1,2,3]
stack = []
lazers = 0
bars = 0
answer = 0
tmp = False
cnt = 0
for x in line:
    print('',stack)
    if stack:
        if stack[-1] == '(':
            if x == '(':
                bars += 1 
            else:
                lazers+=1
        elif stack[-1] == ')':
            if x == '(':
                if bars == 0:
                    cnt = 0
                    while stack and cnt != 2:
                        cnt+=1
                        lazers = 0
                        stack.pop()
                    cnt = 0
            else:
                answer += lazers + 1
                if bars != 0:
                    while stack and cnt != (lazers+1) *2-1:
                        cnt+=1
                        stack.pop()
                cnt = 0
                bars -= 1
                continue
    print(stack, bars, lazers, answer)
    stack.append(x)