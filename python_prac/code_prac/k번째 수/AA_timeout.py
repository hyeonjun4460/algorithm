# 시간초과

import sys
sys.stdin = open('input.txt', 'rt')

n = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

count = n[0][0]

for i in range(1, count+1):
    lists = n[i*2-1]
    testCase = n[i*2]
    s = lists[1]
    e = lists[2]
    k = lists[3]
    result = testCase[s-1:e]
    result.sort()
    number = '$'+str(i)
    print(number,result[k-1])
