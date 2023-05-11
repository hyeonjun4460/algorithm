import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')
formula = list(input())

operators = deque()
answer = ''
tmp = False

# 우선순위가 높은 연산자
# 큐에서 연산자를 꺼내야하는 상황에 대한 정리