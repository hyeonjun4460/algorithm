import sys
sys.stdin = open('input.txt', 'rt')

a = list(range(0,21))
for _ in range(10):
    x,y = map(int, input().split())
    for i in range(y-x+1//2):
        a[x+i], a[y-i] = a[y-i], a[x+i]

a.pop(0)
print(' '.join(map(str,a)))