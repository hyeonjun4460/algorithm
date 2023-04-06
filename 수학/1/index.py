# 문제링크: https://www.acmicpc.net/problem/4375
import sys

lines = sys.stdin.readlines()
data = [int(line.strip()) for line in lines]

for a in data:
    n = '1'
    while True:
        if (int(n)%a == 0):
            print(len(n))
            break
        n += '1'
    
