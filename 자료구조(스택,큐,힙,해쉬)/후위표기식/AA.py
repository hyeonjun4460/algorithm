import sys
from collections import deque
# sys.stdin = open('input.txt', 'rt')
formula = list(input())

operators = deque()
answer = ''
bracket_status = False
bracket = ''
bracket_operators = deque()
# 우선순위가 높은 연산자
# 괄호 안에 있는 기호들
# *, /
# +, -

# 숫자면 answer에 추가
# 기호면 큐에 넣기
# )가 끝나면 answer에 ++하기

for x in formula:
    if bracket_status == False:
        if x != '+' and x != '-' and x != '*' and x != '/' and x != '(' and x !=')':
            answer += x
        else:
            if x == '(':
                # operator 싹 비우기
                bracket_status = True
                continue
            if len(operators) != 0 and operators[0] != "+" and operators[0] != '-':
                    answer += operators.popleft()
            if x == '*' or x == '/':
                operators.appendleft(x)
            else:
                if len(operators) !=0:
                    answer+=operators.popleft()
                operators.append(x)
    else:
        if x != '+' and x != '-' and x != '*' and x != '/' and x != '(' and x !=')':
            bracket += x
        else:
            if x == ')':
                while len(bracket_operators) != 0:
                    bracket += bracket_operators.popleft()
                # bracket operator 싹 비우기
                answer += bracket
                if len(operators) != 0 and operators[0] != "+" and operators[0] != '-':
                    answer += operators.popleft()
                bracket = ''

                bracket_status = False
                continue
            if len(bracket_operators) != 0 and bracket_operators[0] != "+" and bracket_operators[0] != '-':
                    answer += bracket_operators.popleft()
            if x == '*' or x == '/':
                bracket_operators.appendleft(x)
            else:
                if len(bracket_operators) !=0:
                    bracket+=bracket_operators.popleft()
                bracket_operators.append(x)
else:
    while len(operators) != 0:
        answer += operators.popleft()

print(answer)
