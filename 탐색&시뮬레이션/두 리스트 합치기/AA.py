import sys
# sys.stdin = open('input.txt', 'rt')

N = int(input())
list_a = list(map(int,input().split()))
M = int(input())
list_b = list(map(int,input().split()))

list_a += list_b

list_a.sort()
print(' '.join(map(str,list_a)))
