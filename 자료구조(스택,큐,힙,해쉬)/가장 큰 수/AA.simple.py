import sys
sys.stdin = open('input.txt', 'rt')

n,m = input().split()

m = int(m)
N = list(int(x) for x in n)
# cnt 가 m이 될 때까지
# 첫번쨰 값은 스택에 넣는다.
# 스택의 값보다 작으면 pass
# 스택의 값보다 크면 스택 값을 pop하고 새 값을 넣는다.
cnt = 0
stack = []
index = 0

for x in N:
    # 스택이 비어있지 않고, 뺄 수 있는 자리수가 남아있다면
    # 넣을 값이 stack의 마지막 값보다 계속 크다면
    # pop
    while stack and m > 0 and int(stack[-1]) < x:
        stack.pop()
        m -= 1
    # stack이 비어있거나
    # stack의 마지막값이 들어올 값보다 크다면 stack에 넣기
    stack.append(str(x))
# 예외처리: 반복문 마지막까지 순회했는데도 pop이 이루어지지 않을경우
# 스택의 마지막 숫자부터 차례로 빼기
if m != 0:
    stack = stack[:-m]

res = ''.join(x for x in stack)
print(res)