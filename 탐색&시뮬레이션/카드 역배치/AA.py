import sys
sys.stdin = open('input.txt', 'rt')

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(10):
    a,b = map(int, input().split())
    slices = data[a-1:b]
    slices.reverse()
    data[a-1:b] = slices
    print(data)

print(' '.join(map(str,data)))